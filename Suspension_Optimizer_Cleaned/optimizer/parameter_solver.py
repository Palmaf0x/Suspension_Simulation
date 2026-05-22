                   
from optimizer.regime_constraints import *
import numpy as np

                      
def parameter_solver_one(response) :
                        
    if response["parameters"][1] == None and response["parameters"][2] == None :
        k = np.arange(10000, 80000, 1000)
        c = np.arange(500, 10000, 200)
        data = regime_contraintes(response["parameters"][0], k, c, response["regime_wanted"])
        return data
                        
    elif response["parameters"][0] == None and response["parameters"][2] == None :
        m = np.arange(100, 500, 1000)
        c = np.arange(500, 10000, 200)
        data = regime_contraintes(m, response["parameters"][1], c, response["regime_wanted"])
        return data
                        
    elif response["parameters"][0] == None and response["parameters"][1] == None :
        m = np.arange(100, 500, 1000)
        k = np.arange(10000, 80000, 1000)
        data = regime_contraintes(m, k, response["parameters"][2], response["regime_wanted"])
        return data
    
def parameter_solver_two(response) :
                      
    if response["parameters"][2] == None :
        c = np.arange(500, 10000, 200)
        data = regime_contraintes(response["parameters"][0], response["parameters"][1], c, response["regime_wanted"])
        return data 
                     
    elif response["parameters"][1] == None :
        k = np.arange(10000, 80000, 1000)
        data = regime_contraintes(response["parameters"][0], k, response["parameters"][2], response["regime_wanted"])
        return data 
                     
    elif response["parameters"][0] == None :
        m = np.arange(100, 500, 1000)
        data = regime_contraintes(m, response["parameters"][1], response["parameters"][2], response["regime_wanted"])
        return data
    
def parameter_solver_three(response) :
                   
    x = response["parameters"]
    data = regime_contraintes(x[0], x[1], x[2], response["regime_wanted"])
    
def parameter_solver(response) :
    unknow_counter = 0
    for i in response["parameters"] :
        if i == None :
            unknow_counter += 1
    if unknow_counter == 0 :
        return parameter_solver_three(response)
    elif unknow_counter == 1 :
        return parameter_solver_two(response)
    elif unknow_counter == 2 : 
        return parameter_solver_one(response)
           


