import src.api as api
import src.processing as processing
import src.analysis as analysis
import src.visualization as visualization

def run_weather_pipeline(city_name, start_date, end_date):
    lat, lon, country = api.get_coordinates(city_name)
    path = api.fetch_weather_data(lat, lon, city_name, start_date, end_date)
    processed_path = processing.process_weather_data(path, city_name)
    analysis_data = analysis.analyze_weather(processed_path, city_name)

    return analysis_data, visualization.plot_weather_analysis_outputs(analysis_data, city_name),country
