from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
# import the functions
from Suspension_Simulation.optimizer.regime_constraints import *
from Suspension_Simulation.optimizer.parameter_solver import *
from Suspension_Simulation.physics.equations import *
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

    return {"message" : "Data received !!",
            "data" : data_received}
