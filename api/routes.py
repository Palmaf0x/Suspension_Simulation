from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
# import the functions
from optimizer.regime_constraints import *
from optimizer.parameter_solver import *
from physics.equations import *
from optimizer.parameter_solver import *

# creation of the app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # domaines autorisés
    allow_credentials=True,
    allow_methods=["*"],            # GET, POST, etc.
    allow_headers=["*"],            # headers autorisés
)
class data_format(BaseModel):
    parameters: Optional[list] = None
    initial_speed: Optional[float] = None
    initial_position: Optional[float] = None
    regime_wanted: str

@app.post("/send_data")
def send_data(data_received: data_format):
    response = data_received.dict()
    print(response)
    list_data = parameter_solver(response)
    system_parameters = list_data[0]
    plotting_data = equation_finder(response, system_parameters)
    print(plotting_data)
    return {
        "x_values" : plotting_data[0].tolist(),
        "y_values" : plotting_data[1].tolist(),
    }

data_plotting = send_data

@app.get("/get_data")
def get_data():
    return data_plotting