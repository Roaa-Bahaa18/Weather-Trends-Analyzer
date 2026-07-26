import os
import dask.dataframe as dd
from pandas.conftest import dropna


def process_weather_data(city_file_path,city_name):
    ddf = dd.read_parquet(city_file_path)

    #Clean data from missing values
    ddf = ddf.fillna({"precipitation": 0.0})
    ddf = ddf.dropna(subset=["temperature_2m"])

    os.makedirs('data/processed', exist_ok=True)

    file_path = f"data/processed/{city_name.lower()}_weather_cleaned.parquet"
    ddf.to_parquet(file_path, engine='pyarrow',compression="snappy", write_index=False)
    return file_path

