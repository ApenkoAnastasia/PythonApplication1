import sys
from math import *
import numpy as np     
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, radians(1650), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()

# work with git