# importing module
from Suspension_Simulation.physics.equations import *
# cretion of the list for the pandas dataframe
amplitude_list = []
time_stop_list = []
# function to find the amplitude and time stop for every combinasion
def computing_amplitude() :
    list_ampli = []
    list_time = []
    for data in list_data :
        # get values of graph for each list of combinaision
        values = equation_finder(response, data)
        amplitude = max(abs(values[1]))
        list_ampli.append(amplitude)
        min_value = min(values[1])
        # find the time of min "least vibration"
        for x in range(len(values[1])) :
            if values[1][x] == min_value :
                time_stop = values[0][x]
                list_time.append(time_stop)
    return list_ampli, list_time

amplitude_list, time_stop_list = computing_amplitude()

print(time_stop_list)
print(amplitude_list)
