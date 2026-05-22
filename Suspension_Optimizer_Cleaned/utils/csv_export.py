import pandas as pd
                                                   
                    
                                                                       
def csv_maker(list_data, list_amplitude, list_time_stop):
                               
    mass_data = []
    raideur_data = []
    friction_data = []
    for data in list_data :
        mass_data.append(data[0])
        raideur_data.append(data[1])
        friction_data.append(data[2])

                               
    csv_data = {
        "Mass" : mass_data,
        "Raideur" : raideur_data,
        "Friction" : friction_data,
        "Amplitude" : list_amplitude,
        "Time_Stop" : list_time_stop
    }
    return csv_data
