                   
import numpy as np 

                                   
def computing_one_mass(a,x,y, nature) :
                                 
        X,Y = np.meshgrid(x, y)
                                
        delta = Y / (2 * np.sqrt(X * a))
        good_list = []
                              
        if nature == "sous" :
            detector = delta < 1
        elif nature == "critique" :
            detector = delta == 1
        elif nature == "sur" :
            detector = delta > 1
        
        good = np.where(detector)
        for i, j in zip(good[0], good[1]) :
            good_list.append((a, X[i,j], Y[i,j]))
        return good_list
    
def computing_one_raider(a,x,y, nature) :
                                 
        X,Y = np.meshgrid(x, y)
                                
        delta = Y / (2 * np.sqrt(a * X))
        good_list = []
                              
        if nature == "sous" :
            detector = delta < 1
        elif nature == "critique" :
            detector = delta == 1
        elif nature == "sur" :
            detector = delta > 1
        
        good = np.where(detector)
        for i, j in zip(good[0], good[1]) :
            good_list.append((a, X[i,j], Y[i,j]))
        return good_list

def computing_one_friction(a,x,y, nature) :
                                 
        X,Y = np.meshgrid(x, y)
                                
        delta = a / (2 * np.sqrt(X * Y))
        good_list = []
                              
        if nature == "sous" :
            detector = delta < 1
        elif nature == "critique" :
            detector = delta == 1
        elif nature == "sur" :
            detector = delta > 1
        
        good = np.where(detector)
        for i, j in zip(good[0], good[1]) :
            good_list.append((a, X[i,j], Y[i,j]))
        return good_list
    
def computing_two_friction(m, k, c, nature) :
    good_list = []
    for x in c :
        delta = c / (2 * np.sqrt(k*m))
        if delta < 1 and nature == "sous" :
            good_list.append((m, k, c))
        elif delta == 1 and nature == "critique" : 
            good_list.append((m, k, c))
        elif delta > 1 and nature == "sur" :
            good_list.append((m, k, c))
    return good_list

def computing_two_raideur(m, k, c, nature) :
    good_list = []
    for x in k :
        delta = c / (2 * np.sqrt(k*m))
        if delta < 1 and nature == "sous" :
            good_list.append((m, k, c))
        elif delta == 1 and nature == "critique" : 
            good_list.append((m, k, c))
        elif delta > 1 and nature == "sur" :
            good_list.append((m, k, c))
    return good_list

def computing_two_mass(m, k, c, nature) :
    good_list = []
    for x in m :
        delta = c / (2 * np.sqrt(k*m))
        if delta < 1 and nature == "sous" :
            good_list.append((m, k, c))
        elif delta == 1 and nature == "critique" : 
            good_list.append((m, k, c))
        elif delta > 1 and nature == "sur" :
            good_list.append((m, k, c))
    return good_list

def computing_three(m, k, c, nature) :
    good_list = []
                              
    delta = c / (2 * np.sqrt(k*m))
    if delta < 1 and nature == "sous" :
        good_list.append((m, k, c))
    elif delta == 1 and nature == "critique" : 
        good_list.append((m, k, c))
    elif delta > 1 and nature == "sur" :
        good_list.append((m, k, c))
    return good_list

def regime_contraintes(m, k, c, nature) :
    if isinstance(m, (int, float)) :
        return computing_one_mass(m, k, c, nature) 
    
    elif isinstance(k, (int, float)) :
        return computing_one_raider(k, m, c, nature)
    
    elif isinstance(c, (int, float)) :
        return computing_one_friction(c, m, k, nature)
    
    elif isinstance(m, (int,float)) and isinstance(k, (int,float)) :
        return computing_two_friction(m, k, c, nature)
    
    elif isinstance(m, (int,float)) and isinstance(c, (int,float)) :
        return computing_two_raideur(m, k, c, nature)
    
    elif isinstance(k, (int,float)) and isinstance(c, (int,float)) :
        return computing_two_mass(m, k, c, nature)
    elif isinstance(k, (int,float)) and isinstance(c, (int,float)) and isinstance(m, (int, float)) :
        return computing_three(m, k, c, nature)


