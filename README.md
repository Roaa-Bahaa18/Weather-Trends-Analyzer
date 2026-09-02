# 🌦️ Weather-Trends-Analyzer
A scalable data processing pipeline built in Python that automates weather data ingestion from Open-Meteo, leverages Dask for parallel computing, and delivers comprehensive trend analysis and visualizations. 

---

## 🔗 Overview

The Weather Trends Analyzer allows users to select a city and a date range, retrieve historical weather data, and explore trends through data analysis and visualizations.

The project demonstrates how Python can be used to build a complete data-processing pipeline:

```text
Open-Meteo API
       │
       ▼
  Data Ingestion
       │
       ▼
 Data Processing
   Pandas / NumPy
       │
       ▼
 Parallel Processing
       Dask
       │
       ▼
   Data Analysis
       │
       ▼
 Visualizations
       │
       ▼
 Interactive Dashboard
```

---

## 📋 Features

### Interactive Frontend

- Simple and clean interface for weather analysis.
- Allows users to select cities and date ranges.
- Displays processed weather trends and visualizations.

### Weather Data Ingestion

- Retrieves historical weather data from the **Open-Meteo API**.
- Organizes retrieved data for further processing and analysis.

### Data Processing

- Uses **Pandas** for tabular data manipulation and analysis.
- Uses **NumPy** for numerical operations and calculations.
- Uses **Dask DataFrames** for parallel and scalable data processing.
- Uses **Apache Parquet** for efficient storage of processed datasets.

### Weather Trend Analysis

The application can analyze weather variables and identify trends within the selected time period.

Examples include:

- Temperature trends
- Weather measurements over time
- Aggregated weather statistics

### Data Visualization

Processed weather data is transformed into visual representations to make trends easier to understand.

### Input Validation

- Validates city inputs.
- Validates date ranges.
- Prevents users from requesting future dates beyond the available data limits.
- Performs validation on both the frontend and backend.

---

## 💻 Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical operations |
| **Dask** | Parallel and scalable data processing |
| **Apache Parquet** | Efficient processed-data storage |
| **FastAPI** | Backend API and request handling |
| **Uvicorn** | ASGI server |
| **HTML/CSS** | Frontend interface |
| **Open-Meteo API** | Weather data source |

---


## 🏗️ Project Structure
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
## 📚 Prerequisites

Ensure you have the following installed:
* **Python 3.10+**
* **pip** (Python package installer)
---

## 📩 Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd Weather-Trends-Analyzer
```

Create a virtual environment:

```bash
python -m venv venv
```

---

## 👟 Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn app:app --reload
```

Once the server starts, open the application in a web browser using the local address displayed by Uvicorn.

The `--reload` option automatically reloads the application when source files are modified during development.

---

## ❔ Why Dask?

One of the main goals of the project was to explore how data-processing approaches can scale beyond a simple Pandas workflow.

While Pandas is highly effective for many datasets, Dask provides a way to work with larger datasets by dividing computations into smaller tasks that can be executed in parallel.

In this project, Dask was used to demonstrate the transition from:

```text
Single-process data analysis
          │
        Pandas
          │
          ▼
Parallel / scalable processing
          │
        Dask
```

This provided practical exposure to the concepts of **parallel computing and scalable data processing**, which are particularly relevant to HPC environments.

---

