import pandas as pd
# Suspension_Simulation.analysis.amplitude import *
# importing the data
#from Suspension_Simulation.optimizer.parameter_solver import list_data
def csv_maker(list_data, list_amplitude, list_time_stop):
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
        "Amplitude" : list_amplitude,
        "Time_Stop" : list_time_stop
    }
    return csv_data
