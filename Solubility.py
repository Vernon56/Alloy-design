import numpy as np
import pandas as pd
from functools import wraps

max_solubility = {'Al': 100.0,
  'Cu': 2.4,
  'Si': 1.6,
  'Mg': 16.5,
  'Mn': 0.6,
  'Fe': 0.04,
  'Zn': 66.4,
  'Ni': 0.02,
  'Ti': 0.79,
  'Sc': 0.23,
  'Ag': 19,
  'Zr': 0.083,
  'Cr': 0.34,
  'Sb': 0.02,
  'Li': 14.7,
  'Ce': 0.01,
  'La': 0.01,
  'V': 0.33,
  'Co': 0.43,
  'Ca': 0.27,
  'Mo': 0.25,
  'Nb': 0.066,
  'Sn': 0.025,
  'Hf': 0.186,
  'Y':0.049}
  
room_solubility = {'Al': 100.0,
  'Cu': 0.15,
  'Si': 0.05,
  'Mg': 0.55,
  'Mn': 0.001,
  'Fe': 0.001,
  'Zn': 1.3,
  'Ni': 0.001,
  'Ti': 0.001,
  'Sc': 0.001,
  'Ag': 0.1,
  'Zr': 0.001,
  'Cr': 0.001,
  'Sb': 0.001,
  'Li': 0.14,
  'Ce': 0.001,
  'La': 0.001,
  'V': 0.001,
  'Co': 0.001,
  'Ca': 0.001,
  'Mo': 0.001,
  'Nb': 0.001,
  'Sn': 0.001,
  'Hf': 0.001,
  'Y':0.001}

solubility_gap = {'Al': 0.0, 
'Cu': 2.25, 
'Si': 1.55, 
'Mg': 15.95, 
'Mn': 0.599, 
'Fe': 0.039, 
'Zn': 65.100, 
'Ni': 0.019, 
'Ti': 0.789, 
'Sc': 0.229, 
'Ag': 18.9, 
'Zr': 0.082, 
'Cr': 0.339, 
'Sb': 0.019, 
'Li': 14.56, 
'Ce': 0.009, 
'La': 0.009, 
'V': 0.329, 
'Co': 0.429, 
'Ca': 0.269, 
'Mo': 0.249, 
'Nb': 0.065, 
'Sn': 0.024, 
'Hf': 0.185, 
'Y': 0.048}
 
def check(func):
    @wraps(func)
    def wrapper(x,**kwargs):
        
        if set(list(x.index)) <= set(list(solubility_gap.keys())):
            return func(x,**kwargs)
        else:
            print('Please check your columns and make sure all columns’ name are elements')
            raise Exception(ImportError)
    return wrapper

@check
def max_sb(x, decimal = 3):
    el = list(x.index)
    if 'Al' in el:
        el.remove('Al')
    else:
        pass
    value = [x[i]*max_solubility[i] for i in el]
    value = sum(value)
    return value
            

@check
def room_sb(x, decimal = 3):
    el = list(x.index)
    if 'Al' in el:
        el.remove('Al')
    else:
        pass
    value = [x[i]*room_solubility[i] for i in el]
    value = sum(value)
    return value

@check
def sb_gap(x, decimal = 3):
    el = list(x.index)
    if 'Al' in el:
        el.remove('Al')
    else:
        pass
    value = [x[i]*max_solubility[i]-x[i]*room_solubility[i] for i in el]
    value = sum(value)
    return value
    