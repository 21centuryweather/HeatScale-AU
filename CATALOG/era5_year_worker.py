
import gc
import os
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr


# ============================================================
# ERA5 NetCDF utilities
# ============================================================

def find_data_variable(ds):
    """Return the principal time-latitude-longitude data variable."""

    candidates = [
        name
        for name, da in ds.data_vars.items()
        if (
            "time" in da.dims
            and "latitude" in da.dims
            and "longitude" in da.dims
        )
    ]

    if len(candidates) != 1:
        raise ValueError(
            f"Expected one ERA5 data variable, found {candidates}"
        )

    return candidates[0]


# ============================================================
# ERA5 dew point -> specific humidity
# ============================================================

def huss_from_dewpoint(td, ps):
    """
    Convert ERA5 2 m dew-point temperature and surface pressure
    to specific humidity.

    Parameters
    ----------
    td : array
        2 m dew-point temperature [K]
    ps : array
        Surface pressure [Pa]

    Returns
    -------
    q : float32 array
        Specific humidity [kg kg-1]
    """

    td = np.asarray(td, dtype=np.float64)
    ps = np.asarray(ps, dtype=np.float64)

    Rd = 287.0597
    Rv = 461.5250
    epsilon = Rd / Rv

    a1 = 611.21
    a3 = 17.502
    a4 = 32.19
    T0 = 273.16

    # Vapour pressure from dew-point temperature.
    e = a1 * np.exp(
        a3 * (td - T0) / (td - a4)
    )

    # Specific humidity.
    q = (
        epsilon * e
        / (ps - (1.0 - epsilon) * e)
    )

    return q.astype(np.float32)


# ============================================================
# Read one source variable for one month
# ============================================================

def load_variable(paths, target_times, lat_slice, lon_slice):
    """Read and concatenate all matching data for one ERA5 source field."""

    target_times = pd.DatetimeIndex(target_times)

    data_parts = []
    time_parts = []

    for path in paths:
        with xr.open_dataset(
            path,
            decode_times=True,
            cache=False,
        ) as ds:
            varname = find_data_variable(ds)

            da = ds[varname].transpose(
                "time",
                "latitude",
                "longitude",
            )

            file_times = pd.DatetimeIndex(
                pd.to_datetime(ds["time"].values)
            )

            idx = np.where(
                file_times.isin(target_times)
            )[0]

            if len(idx) == 0:
                continue

            # Monthly ERA5 files are normally contiguous in time.
            if len(idx) == 1 or np.all(np.diff(idx) == 1):
                time_selector = slice(
                    int(idx[0]),
                    int(idx[-1] + 1),
                )
            else:
                time_selector = idx

            values = da.isel(
                time=time_selector,
                latitude=slice(*lat_slice),
                longitude=slice(*lon_slice),
            ).values

            data_parts.append(
                np.asarray(values, dtype=np.float32)
            )
            time_parts.append(file_times[idx].values)

    if not data_parts:
        raise RuntimeError("No matching ERA5 data were found.")

    data = np.concatenate(data_parts, axis=0)
    times = np.concatenate(time_parts)

    order = np.argsort(times)
    times = pd.DatetimeIndex(times[order])
    data = data[order]

    if not times.equals(target_times):
        missing = target_times.difference(times)
        extra = times.difference(target_times)
        raise RuntimeError(
            f"ERA5 datetime mismatch: missing={len(missing)}, extra={len(extra)}"
        )

    return data


# ============================================================
# Process one complete calendar year
# ============================================================

def process_year(task):
    year = int(task["year"])
    out_dir = Path(task["out_dir"])

    final_path = out_dir / f"{year}.npy"
    partial_path = out_dir / f"{year}.partial.npy"

    try:
        if final_path.exists() and not task["overwrite"]:
            return {
                "year": year,
                "status": "SKIPPED",
                "hours": len(task["times"]),
                "file": str(final_path),
                "error": None,
            }

        if partial_path.exists():
            partial_path.unlink()

        times = pd.DatetimeIndex(task["times"])

        ntime = len(times)
        nlat = int(task["nlat"])
        nlon = int(task["nlon"])

        lat_slice = tuple(task["lat_slice"])
        lon_slice = tuple(task["lon_slice"])

        # Each record contains its datetime and a (9, lat, lon) matrix.
        sample_dtype = np.dtype(
            [
                ("datetime", "datetime64[ns]"),
                ("data", np.float32, (9, nlat, nlon)),
            ]
        )

        year_data = np.empty(
            ntime,
            dtype=sample_dtype,
        )

        year_data["datetime"] = times.values.astype(
            "datetime64[ns]"
        )

        # ----------------------------------------------------
        # Fill the full year month by month.
        # ----------------------------------------------------
        for month in range(1, 13):
            month_mask = times.month == month
            positions = np.where(month_mask)[0]

            if len(positions) == 0:
                raise RuntimeError(
                    f"{year}-{month:02d}: no timestamps found"
                )

            start = int(positions[0])
            stop = int(positions[-1] + 1)
            month_times = times[month_mask]

            paths = task["month_paths"][month]

            # Native ERA5 source fields.
            t2 = load_variable(
                paths["2t"], month_times, lat_slice, lon_slice
            )
            td2 = load_variable(
                paths["2d"], month_times, lat_slice, lon_slice
            )
            sp = load_variable(
                paths["sp"], month_times, lat_slice, lon_slice
            )
            u10 = load_variable(
                paths["10u"], month_times, lat_slice, lon_slice
            )
            v10 = load_variable(
                paths["10v"], month_times, lat_slice, lon_slice
            )
            sw_down = load_variable(
                paths["msdwswrf"], month_times, lat_slice, lon_slice
            )
            sw_net = load_variable(
                paths["msnswrf"], month_times, lat_slice, lon_slice
            )
            lw_down = load_variable(
                paths["msdwlwrf"], month_times, lat_slice, lon_slice
            )
            lw_net = load_variable(
                paths["msnlwrf"], month_times, lat_slice, lon_slice
            )

            out = year_data["data"][start:stop]

            # Fixed target-variable order:
            # 0 tas, 1 huss, 2 ps, 3 uas, 4 vas,
            # 5 rsds, 6 rsus, 7 rlds, 8 rlus
            out[:, 0] = t2
            out[:, 1] = huss_from_dewpoint(td2, sp)
            out[:, 2] = sp
            out[:, 3] = u10
            out[:, 4] = v10
            out[:, 5] = sw_down

            # Surface net shortwave = downward - upward.
            out[:, 6] = sw_down - sw_net

            out[:, 7] = lw_down

            # Surface net longwave = downward - upward.
            out[:, 8] = lw_down - lw_net

            del (
                t2,
                td2,
                sp,
                u10,
                v10,
                sw_down,
                sw_net,
                lw_down,
                lw_net,
                out,
            )
            gc.collect()

        # Write a complete year to a temporary name first.
        np.save(
            partial_path,
            year_data,
            allow_pickle=False,
        )

        del year_data
        gc.collect()

        # Publish only after the complete yearly file has been written.
        os.replace(partial_path, final_path)

        return {
            "year": year,
            "status": "OK",
            "hours": ntime,
            "file": str(final_path),
            "error": None,
        }

    except Exception as exc:
        if partial_path.exists():
            try:
                partial_path.unlink()
            except Exception:
                pass

        return {
            "year": year,
            "status": "FAILED",
            "hours": len(task.get("times", [])),
            "file": None,
            "error": repr(exc),
        }
