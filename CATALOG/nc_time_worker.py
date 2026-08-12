
import pandas as pd
import xarray as xr


def extract_file_datetimes(path):
    try:
        with xr.open_dataset(
            path,
            decode_times=True,
            cache=False
        ) as ds:

            times = pd.to_datetime(ds["time"].values)

        return path, times, None

    except Exception as e:
        return path, None, repr(e)

