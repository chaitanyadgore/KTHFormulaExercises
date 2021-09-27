import matplotlib.pyplot as plt
import math
import numpy as np


class HClass:
    list=[]

    def __init__(self, t):
        self.t=t


    def Lambda(self,p):

            #print(np.sin(2*(np.pi)*p))
            L= 5*(np.sin(2*(np.pi)*p))
            return L

    def h(self):
        
        for p in range(self.t):
            y= 3*np.pi*np.exp(-self.Lambda(p))
            self.list.append(y)

    def plot(self):
            plt.plot(self.list)
            plt.ylabel('The Function: 3*np.pi*np.exp(-5*(np.sin(2*(np.pi)*p)))')
            plt.show()

    def print_list(self):
            print(self.list)

p1=HClass(100)
p1.h()
p1.print_list()
p1.plot()
#print(p1.list)
#plt.plot(list)            