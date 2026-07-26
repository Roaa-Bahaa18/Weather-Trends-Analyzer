import os

import matplotlib.pyplot as plt
import pandas as pd

def plot_weather_analysis_outputs(analyzed_data,city_name):

    fig, axes = plt.subplots(3, 1, figsize=(12, 14),gridspec_kw={'height_ratios': [1, 1, 2]})
    plt.subplots_adjust(hspace=0.35)

    df = analyzed_data["hourly_temp"].copy()
    df["date"] = df["time"].dt.date
    df["hour"] = df["time"].dt.hour
    heatmap = df.pivot_table(index="date", columns="hour", values="temperature_2m")

    img = axes[0].imshow(heatmap)
    axes[0].set_title("Hourly Temperature Trend (°C)")
    axes[0].set_ylabel("°C")
    axes[0].set_xlabel("Hour of Day")

    daily = analyzed_data["daily"].copy()

    axes[1].plot(daily.index, daily['mean_temp'], color='black', linewidth=1.5, label='Daily Avg')
    axes[1].plot(daily.index, daily['max_temp'], color='red', alpha=0.5, linestyle='--',label='Daily Max')
    axes[1].plot(daily.index, daily['min_temp'], color='blue', alpha=0.5, linestyle='--',label='Daily Min')

    axes[1].set_title("Daily Temperature Range (°C)")
    axes[1].set_ylabel("°C")
    axes[1].set_xlabel("Date")

    axes[2].bar(daily.index,daily["precipitation"],color='blue', alpha=0.5, label='Daily Precipitation')
    axes[2].set_title("Daily Precipitation Range (mm)")
    axes[2].set_ylabel("mm")
    axes[2].set_xlabel("Date")

    os.makedirs("static/images", exist_ok=True)
    chart_path = f"static/images/{city_name}_dashboard.png"
    plt.savefig(chart_path, bbox_inches="tight")
    plt.close()
    return chart_path
