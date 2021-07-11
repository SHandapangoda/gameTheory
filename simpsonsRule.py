import numpy as np
import matplotlib.pyplot as plt

def simpsons(fun,a,b,N = 50):

    if N%2 == 1:
        raise ValueError('N should be even')
    
    dx = (b - a) / N

    x = np.linspace(a,b,N+1)
    y = fun(x)

    s = dx/3 * np.sum(y[0: -1: 2] + 4 * y[1: :2] + y[2 : : 2])
    return s

print(simpsons(lambda x : 3 * x ** 2,0,1,10))

