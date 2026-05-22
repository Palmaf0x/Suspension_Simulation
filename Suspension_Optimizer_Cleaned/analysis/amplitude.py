                  
from physics.equations import *
                                              
amplitude_list = []
time_stop_list = []
                                                                    
def computing_amplitude(list_data, response) :
    list_ampli = []
    list_time = []
    for data in list_data :
                                                           
        values = equation_finder(response, data)
        amplitude = max(abs(values[1]))
        list_ampli.append(amplitude)
        min_value = min(values[1])
                                                
        for x in range(len(values[1])) :
            if values[1][x] == min_value :
                time_stop = values[0][x]
                list_time.append(time_stop)
    return list_ampli, list_time


