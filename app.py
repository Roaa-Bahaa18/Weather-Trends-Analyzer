from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import date

from pandas.core.methods.to_dict import to_dict

from src.pipeline import run_weather_pipeline

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse(request,"index.html", {"request": request, "today": date.today()})

@app.post("/analyze")
async def pipeline(request: Request, city: str = Form(...), start_date: date = Form(...), end_date: date = Form(...)):
    today = date.today()
    if start_date > today or end_date > today:
        raise HTTPException(status_code=400, detail="Dates cannot exceed the current date.")

    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date cannot be after the end date.")

    stats,chart_path,country = run_weather_pipeline(city_name=city, start_date=start_date, end_date=end_date)
    return templates.TemplateResponse(request,"dashboard.html", {"request": request, "city": city,"stats": stats, "chart_path": chart_path,"country": country})

if __name__ == "__pipeline__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)