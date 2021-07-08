import random 
import numpy as np
import math
import matplotlib.pyplot as plt
from IPython.display import clear_output

PI = 3.1415626
e = 2.71828

def get_rand_num(min,max):

    range = max - min
    selection = random.uniform(0,1)
    return min + selection * range

def function(x):
    return (e ** (-1 * x) / (1 + (x - 1) ** 2))


def samplingMonte(no_samples = 5000):


    upper_boundry = 5
    lower_boundry = 0
    total_samples = 0

    for i in range(no_samples):
        x = get_rand_num(lower_boundry,upper_boundry)
        total_samples = function(x)
    
    return (upper_boundry - lower_boundry) * float(total_samples / no_samples)

def meanVariance(no_samples):

    max = 5

    run_total = 0

    for in range(no_samples):
        x = get_rand_num(0,max)

        run_total += function(x) ** 2
    sq_sum = run_total ** 2 / no_samples

    run_total = 0

    for i in range(no_samples):
        x = get_rand_num(0, max)

        run_total = function(x)
    sq_avg = (max * run_total / no_samples) ** 2

    return sq_sum - sq_avg

     




