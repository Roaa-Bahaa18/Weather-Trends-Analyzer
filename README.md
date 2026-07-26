# Weather-Trends-Analyzer
A scalable data processing pipeline built in Python that automates weather data ingestion from Open-Meteo, leverages Dask for parallel computing, and delivers comprehensive trend analysis and visualizations. 

## Features
* **Interactive Frontend:** Simple, clean user interface centered around weather analytics.
* **FastAPI Backend:** Robust backend routing with automatic validation for city inputs and date boundaries.
* **Parallel Data Processing:** Utilizes **Dask Dataframes** and **Apache Parquet** for fast, memory-efficient data processing and aggregation.
* **Date Validation:** Frontend and backend guards to prevent selecting future dates beyond current limits.

## Project Structure
```text
Weather-Trends-Analyzer/
│
├── data/
│   ├── raw/                 
│   └── processed/           
│
├── src/
│   ├── analysis.py          
│   ├── pipeline.py
|   ├── api.py
|   ├── visualization.py
│   └── processing.py        
│
├── static/
|   ├── images/
│   └── styles.css
│
├── templates/
│   ├── index.html           
│   └── dashboard.html       
│
└── app.py
```
## Prerequisites

Ensure you have the following installed:
* **Python 3.10+**
* **pip** (Python package installer)

## Run the Application
* uvicorn app:app --reload
