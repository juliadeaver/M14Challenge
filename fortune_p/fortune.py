import pandas as pd
import numpy as np

def fortune(name,age):
    '''
    This function gives you a fortune based on your age
    Parameters: name, give the function your name
                age, the integer that is your age
    Return: None
    '''
    if age <10:
        print(name + ", you will get some ice cream today")
    elif age <20:
        print(name + ", your future will be bright")
    elif age < 25:
        print(name + ", your will have a birthday within the next year")
    elif age < 40:
        print(name + ", you have a big promotion coming your way!")
    elif age < 60:
        print(name + ", Your will come into some money")
    elif age < 100:
        print(name + ", Congrats!! You are still alive.")
    else:
        print(name + ", smuckers will contact you soon!")
        
