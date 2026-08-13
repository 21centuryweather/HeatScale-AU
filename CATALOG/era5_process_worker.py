
import gc
import numpy as np
import pandas as pd
import xarray as xr


TARGET_VARIABLES = [
    "tas",
    "huss",
    "ps",
    "uas",
    "vas",
    "rsds",
    "rsus",
    "rlds",
    "rlus",
]


def find_main_data_variable(ds):

    candidates = []

    for name, da in ds.data_vars.items():

        if (
            "time" in da.dims
            and "latitude" in da.dims
            and "longitude" in da.dims
        ):
            candidates.append(name)

    if len(candidates) != 1:

        raise ValueError(
            f"Expected one main variable, "
            f"found: {candidates}"
        )

    return candidates[0]


def huss_from_dewpoint(td, ps):
    """
    ERA5 2-m specific humidity from:
        td = 2-m dewpoint temperature [K]
        ps = surface pressure [Pa]

    ECMWF Tetens saturation-over-water formulation.

    Returns:
        specific humidity [kg kg-1]
    """

    td = td.astype(
        np.float64,
        copy=False
    )

    ps = ps.astype(
        np.float64,
        copy=False
    )

    # ECMWF constants
    Rd = 287.0597
    Rv = 461.5250

    a1 = 611.21
    a3 = 17.502
    a4 = 32.19
    T0 = 273.16

    epsilon = Rd / Rv

    # Actual vapour pressure equals saturation
    # vapour pressure at dewpoint temperature.
    e = a1 * np.exp(
        a3 * (td - T0) /
        (td - a4)
    )

    q = (
        epsilon * e
        /
        (
            ps
            - (1.0 - epsilon) * e
        )
    )

    return q.astype(
        np.float32
    )


def load_era5_variable(
    paths,
    target_times,
    bbox
):
    """
    Load one ERA5 source variable for one month.

    Multiple paths are supported in case a month is
    split across more than one NetCDF file.
    """

    target_times = pd.DatetimeIndex(
        target_times
    )

    pieces = []

    expected_lat = None
    expected_lon = None

    for path in paths:

        with xr.open_dataset(
            path,
            decode_times=True,
            cache=False
        ) as ds:

            varname = find_main_data_variable(
                ds
            )

            da = ds[varname]

            file_times = pd.DatetimeIndex(
                pd.to_datetime(
                    ds["time"].values
                )
            )

            # Times from this file that belong to
            # the requested month.
            mask = file_times.isin(
                target_times
            )

            idx_time = np.where(
                mask
            )[0]

            if len(idx_time) == 0:
                continue

            lat = ds[
                "latitude"
            ].values

            lon = ds[
                "longitude"
            ].values

            lat_idx = np.where(
                (lat >= bbox["lat_min"]) &
                (lat <= bbox["lat_max"])
            )[0]

            lon_idx = np.where(
                (lon >= bbox["lon_min"]) &
                (lon <= bbox["lon_max"])
            )[0]

            if (
                len(lat_idx) == 0
                or len(lon_idx) == 0
            ):
                raise ValueError(
                    f"No cells inside bbox: {path}"
                )

            lat_slice = slice(
                lat_idx[0],
                lat_idx[-1] + 1
            )

            lon_slice = slice(
                lon_idx[0],
                lon_idx[-1] + 1
            )

            this_lat = lat[
                lat_slice
            ]

            this_lon = lon[
                lon_slice
            ]

            if expected_lat is None:

                expected_lat = this_lat
                expected_lon = this_lon

            else:

                if not np.array_equal(
                    expected_lat,
                    this_lat
                ):
                    raise ValueError(
                        f"Latitude grid mismatch: {path}"
                    )

                if not np.array_equal(
                    expected_lon,
                    this_lon
                ):
                    raise ValueError(
                        f"Longitude grid mismatch: {path}"
                    )

            # Usually the required times are contiguous.
            if np.all(
                np.diff(idx_time) == 1
            ):

                time_selector = slice(
                    idx_time[0],
                    idx_time[-1] + 1
                )

            else:

                time_selector = idx_time

            values = da.isel(
                time=time_selector,
                latitude=lat_slice,
                longitude=lon_slice
            ).values

            values = np.asarray(
                values,
                dtype=np.float32
            )

            selected_times = file_times[
                idx_time
            ]

            pieces.append(
                (
                    selected_times,
                    values
                )
            )

    if len(pieces) == 0:

        raise ValueError(
            "No matching data found"
        )

    all_times = pd.DatetimeIndex(
        np.concatenate([
            p[0].values
            for p in pieces
        ])
    )

    all_data = np.concatenate(
        [
            p[1]
            for p in pieces
        ],
        axis=0
    )

    order = np.argsort(
        all_times.values
    )

    all_times = all_times[
        order
    ]

    all_data = all_data[
        order
    ]

    if not all_times.equals(
        target_times
    ):

        missing = target_times.difference(
            all_times
        )

        extra = all_times.difference(
            target_times
        )

        raise ValueError(
            f"Datetime mismatch. "
            f"Missing={len(missing)}, "
            f"extra={len(extra)}"
        )

    return all_data


def process_month(task):

    year = task["year"]
    month = task["month"]

    try:

        times = pd.DatetimeIndex(
            task["times"]
        )

        paths = task[
            "paths"
        ]

        bbox = task[
            "bbox"
        ]

        output_path = task[
            "output_path"
        ]

        start = task[
            "start"
        ]

        stop = task[
            "stop"
        ]

        # ------------------------------------------------
        # Load native ERA5 inputs
        # ------------------------------------------------

        t2 = load_era5_variable(
            paths["2t"],
            times,
            bbox
        )

        td2 = load_era5_variable(
            paths["2d"],
            times,
            bbox
        )

        sp = load_era5_variable(
            paths["sp"],
            times,
            bbox
        )

        u10 = load_era5_variable(
            paths["10u"],
            times,
            bbox
        )

        v10 = load_era5_variable(
            paths["10v"],
            times,
            bbox
        )

        sw_down = load_era5_variable(
            paths["msdwswrf"],
            times,
            bbox
        )

        sw_net = load_era5_variable(
            paths["msnswrf"],
            times,
            bbox
        )

        lw_down = load_era5_variable(
            paths["msdwlwrf"],
            times,
            bbox
        )

        lw_net = load_era5_variable(
            paths["msnlwrf"],
            times,
            bbox
        )

        # ------------------------------------------------
        # Convert into BARRA-compatible variable set
        # ------------------------------------------------

        tas = t2

        huss = huss_from_dewpoint(
            td2,
            sp
        )

        ps = sp

        uas = u10
        vas = v10

        rsds = sw_down

        # ECMWF net flux is downward positive:
        # net = downward - upward
        rsus = (
            sw_down
            - sw_net
        )

        rlds = lw_down

        rlus = (
            lw_down
            - lw_net
        )

        # ------------------------------------------------
        # Final order:
        #
        # tas
        # huss
        # ps
        # uas
        # vas
        # rsds
        # rsus
        # rlds
        # rlus
        # ------------------------------------------------

        data = np.stack(
            [
                tas,
                huss,
                ps,
                uas,
                vas,
                rsds,
                rsus,
                rlds,
                rlus,
            ],
            axis=1
        ).astype(
            np.float32,
            copy=False
        )

        # Expected:
        # time × variable × lat × lon

        if data.shape[1] != 9:

            raise ValueError(
                f"Wrong variable dimension: "
                f"{data.shape}"
            )

        if data.shape[0] != len(
            times
        ):

            raise ValueError(
                f"Wrong time dimension: "
                f"{data.shape}"
            )

        # ------------------------------------------------
        # Write directly into the yearly NumPy memmap.
        #
        # No huge data array is returned to parent.
        # ------------------------------------------------

        mm = np.load(
            output_path,
            mmap_mode="r+"
        )

        mm["data"][
            start:stop
        ] = data

        mm.flush()

        del mm
        del data

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
        )

        gc.collect()

        return {
            "year": year,
            "month": month,
            "n_times": len(times),
            "status": "OK",
            "error": None,
        }

    except Exception as e:

        return {
            "year": year,
            "month": month,
            "n_times": 0,
            "status": "FAILED",
            "error": repr(e),
        }
