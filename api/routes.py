from __future__ import annotations

from pathlib import Path
from typing import Optional

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from analysis.amplitude import computing_amplitude
from optimizer.parameter_solver import parameter_solver
from physics.equations import equation_finder
from utils.csv_export import csv_maker


app = FastAPI(title="Suspension Simulation API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DataFormat(BaseModel):
    parameters: list[Optional[float]] = Field(..., min_length=3, max_length=3)
    initial_speed: Optional[float] = 0.0
    initial_position: Optional[float] = 0.0
    regime_wanted: str


data_plotting = {"x_values": [], "y_values": []}
list_data_res = []
response_user: dict = {}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/send_data")
def send_data(data_received: DataFormat):
    global list_data_res, response_user
    response = data_received.model_dump()
    try:
        list_data = parameter_solver(response)
        if not list_data:
            raise ValueError("No parameter combination matches the requested regime.")
        system_parameters = list_data[0]
        x_values, y_values = equation_finder(response, system_parameters)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    response_user = response
    list_data_res = list_data
    data_plotting["x_values"] = x_values.tolist()
    data_plotting["y_values"] = y_values.tolist()
    return {
        "message": "Data received",
        "x_values": data_plotting["x_values"],
        "y_values": data_plotting["y_values"],
        "matches": len(list_data),
    }


@app.get("/get_data")
def get_data():
    if not data_plotting["x_values"]:
        raise HTTPException(status_code=404, detail="Run a simulation before requesting data.")
    return data_plotting


@app.get("/download_csv")
def download_csv():
    if not list_data_res or not response_user:
        raise HTTPException(status_code=404, detail="Run a simulation before downloading data.")
    amplitudes, time_stops = computing_amplitude(list_data_res, response_user)
    csv_data = csv_maker(list_data_res, amplitudes, time_stops)
    file_path = Path(__file__).resolve().parent.parent / "csv_data.csv"
    pd.DataFrame(csv_data).to_csv(file_path, index=False)
    return FileResponse(file_path, media_type="text/csv", filename="suspension_simulation.csv")
