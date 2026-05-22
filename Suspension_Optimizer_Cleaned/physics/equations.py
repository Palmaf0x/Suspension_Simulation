               
import numpy as np
                       

                                 
def equation_sous_regime(tuple, pos, speed) : 
                                  
    delta = tuple[2] / (2 * np.sqrt(tuple[0] * tuple[1]))
    pulsation = np.sqrt(tuple[1] / tuple[0])
    zelta = pulsation * np.sqrt(1 - delta**2)
    
                                
    A = pos 
    B = (speed + delta * pulsation * pos) / zelta
    
                      
    settling_time = 4 / (delta * pulsation)
    t_max = 5 * settling_time
    t = np.linspace(0, t_max, 1000)
    y = np.exp(-(delta * pulsation * t)) *  ((A * np.cos(zelta*t) + B * np.sin(zelta*t)))
    return t,y

def equation_critique_regime(tuple, pos, speed) :
                                    
    pulsation = np.sqrt(tuple[1] / tuple[0])
    delta = tuple[2] / (2 * np.sqrt(tuple[0] * tuple[1]))
                                
    A = pos 
    B = speed + pulsation * A
                      
                                
    settling_time = 4 / (delta * pulsation)
    t_max = 5 * settling_time
    t = np.arange(0, t_max, 0.01)
    y = (A + B*t) * np.exp(-1 * pulsation * t)
    return t, y
        

def equation_sur_regime(tuple, pos, speed) :
                                  
    delta = tuple[2] / (2 * np.sqrt(tuple[0] * tuple[1]))
    pulsation = np.sqrt(tuple[1] / tuple[0])                              

                                
    r1 = (-pulsation) * (delta + np.sqrt(delta**2 - 1))
    r2 = (-pulsation) * (delta - np.sqrt(delta**2 - 1))

    A = (speed - r2 * pos) / (r1 - r2)
    B = (r1 * pos - speed) / (r1 - r2)

                      
                                
    settling_time = 4 / (delta * pulsation)
    t_max = 5 * settling_time
    t = np.arange(0, t_max, 0.01)
    y = A * np.exp(r1*t) + B * np.exp(r2*t)
    return t, y
    
    
def equation_finder(response, system_parameters) :
                                        
    if response["regime_wanted"] == "sous" :
        return equation_sous_regime(system_parameters, response["initial_position"], response["initial_speed"])

    elif response["regime_wanted"] == "critique" :
        return equation_critique_regime(system_parameters, response["initial_position"], response["initial_speed"])

    elif response["regime_wanted"] == "sur" :
        return equation_sur_regime(system_parameters, response["initial_position"], response["initial_speed"])

