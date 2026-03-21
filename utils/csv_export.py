import pandas as pd
from Suspension_Simulation.analysis.amplitude import *
# importing the data
from Suspension_Simulation.optimizer.parameter_solver import list_data

# seperation list of values
mass_data = []
raideur_data = []
friction_data = []
for data in list_data :
    mass_data.append(data[0])
    raideur_data.append(data[1])
    friction_data.append(data[2])

# creation of the dataframe
csv_data = {
    "Mass" : mass_data,
    "Raideur" : raideur_data,
    "Friction" : friction_data,
    "Amplitude" : amplitude_list,
    "Time_Stop" : time_stop_list
}

df = pd.DataFrame(csv_data)
df.to_csv("csv_data.csv")
print(df)