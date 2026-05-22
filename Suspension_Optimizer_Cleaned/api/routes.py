from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import FileResponse
                      
from optimizer.regime_constraints import *
from optimizer.parameter_solver import *
from physics.equations import *
from optimizer.parameter_solver import *
from analysis.amplitude import *
from utils.csv_export import *
from analysis.amplitude import *

                     
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],                              
    allow_credentials=True,
    allow_methods=["*"],                             
    allow_headers=["*"],                               
)

                                   
class data_format(BaseModel):
    parameters: Optional[list] = None
    initial_speed: Optional[float] = None
    initial_position: Optional[float] = None
    regime_wanted: str

                                   
data_plotting = {}
list_data_res = []
response_user =  {}
@app.post("/send_data")
def send_data(data_received: data_format):
    global list_data_res, response_user
    response = data_received.dict()
    response_user = response                                        
    list_data = parameter_solver(response)
    list_data_res = list_data                                                   
    system_parameters = list_data[0]
    plotting_data = equation_finder(response, system_parameters)
    data_plotting["x_values"] = plotting_data[0]                                         
    data_plotting["y_values"] = plotting_data[1]                                         
    print(data_plotting)
    return {"message": "Data received!!"}

@app.get("/get_data")
def get_data():
    return {
        "x_values": data_plotting["x_values"].tolist(),
        "y_values": data_plotting["y_values"].tolist(),
    }

@app.get("/download_csv")
def download_csv():
    response = response_user

    amplitude_list, time_stop_list = computing_amplitude(list_data_res, response)

    csv_data = csv_maker(list_data_res, amplitude_list, time_stop_list)
    df = pd.DataFrame(csv_data)

    file_path = "csv_data.csv"
    df.to_csv(file_path, index=False)

    return FileResponse(file_path, media_type="text/csv", filename="data.csv")
