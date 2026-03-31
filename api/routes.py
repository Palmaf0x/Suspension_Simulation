from fastapi import FastAPI
from pydantic import BaseModel

# creation of the app
app = FastAPI()

response = {
    "parameters" : [500, None, None],
    "initial_position" : 5,
    "initial_speed" : 2,
    "regime_wanted" : "sous"
}