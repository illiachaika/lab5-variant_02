"""
LabWork #5: "Functions and task decomposition 
Variant: 2
Student: [Chaika, Illia]
Group: [EIP30(1)]
"""
import math

def phi(x:float)-> float:
    return  x-(math.log(x)-1/(1+x**2)) #Function to use for futher iterations

