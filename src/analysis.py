import dask.dataframe as dd


def analyze_weather(file_path, city_name):
    ddf = dd.read_parquet(file_path, engine='pyarrow')
    ddf["time"] = dd.to_datetime(ddf["time"])
    ddf["date"] = ddf["time"].dt.floor("D")

    hourly_ddf = ddf[["time", "temperature_2m"]]
    daily_ddf = (
        ddf.groupby("date")
        .agg({
            "temperature_2m": ["mean", "max", "min"],
            "precipitation": "sum"
        })
    )

    hourly_temp, daily, overall_stats = dd.compute(
        hourly_ddf,
        daily_ddf,
        {
            "mean_temp": ddf.temperature_2m.mean(),
            "max_temp": ddf.temperature_2m.max(),
            "min_temp": ddf.temperature_2m.min(),
            "precipitation": ddf.precipitation.sum(),
        }
    )
    daily.columns = ["mean_temp", "max_temp", "min_temp", "precipitation"]

    output = {
        "city": city_name,
        "hourly_temp": hourly_temp,
        "daily": daily,
        "mean_temp": overall_stats["mean_temp"],
        "max_temp": overall_stats["max_temp"],
        "min_temp": overall_stats["min_temp"],
        "precipitation": overall_stats["precipitation"],
    }

    return output