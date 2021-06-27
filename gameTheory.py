import numpy as np 
from random import random
import matplotlib.pyplot as plt

def calcPi():

    points_on_circle = 0
    total_points = 1000000

    xPo = np.zeros(total_points)
    yPo = np.zeros(total_points)

    x_circle = []
    y_circle = []

    for i in range(total_points):
        x = -1 + 2*random()
        y = -1 + 2*random()

        if((x ** 2 + y ** 2) <= 1):
            points_on_circle = points_on_circle + 1
            x_circle.append(x)
            y_circle.append(y)
    
        xPo[i] = x
        yPo[i] = y

    pi = 4 * points_on_circle / total_points
    print("Pi =", pi)
    plt.plot(xPo,yPo,'.', color='green')
    plt.plot(x_circle,y_circle,'.', color='red')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.gca().set_title('y vs x')
    plt.show()

def randomSampling():

    a = 0 
    b = 5

    x = 5 
    max_Px = 3 * x / 5 + 2

    M = 0 # dots inside rectangle assumed
    N = 1000 #number of tests
    x_total = np.zeros(N)
    y_total = np.zeros(N)

    x_region = []
    y_region = []
    for i in range(N):

        x = a + (b - a) * random()
        y = 0 + (max_Px - 0) * random()

        Y_value = 3 * x / 5 + 2

        if(Y_value >= y):
            M = M + 1
            x_region.append(i)
            y_region.append(i)

        x_total[i] = x
        y_total[i] = y
    Area = max_Px * (b - a)* M / N
    print(Area)
    plt.plot(x_region, y_region, '.' , color='green')
    plt.plot(x_total,y_total, '.', color='blue')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

randomSampling()