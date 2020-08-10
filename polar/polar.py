#!/usr/bin/env python3

import random
import sys

import matplotlib.pyplot as plt
import numpy as np

import autograd.numpy as anp

from autograd import elementwise_grad as egrad

sys.path.append('../modules')

from geometry import *
from graphing import *
from data import *

def normalize(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle(v1, v2):
    v1_u = normalize(v1)
    v2_u = normalize(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

# Creating the data set
size = 25
mx = 5

D = uniform_data_set(size, -mx, mx, -mx, mx)

cuh = convex_upper_hull(D)
clh = convex_lower_hull(D)

hull = cuh + clh

# Plotting
t = np.arange(0, mx, 0.01)

plot(D, 'cx')
plot(p_D, 'bx')

plot(clh, 'y-')
plot(cuh, 'y-')
plot(p_cuh, 'g-')
plot(p_cuh, 'g-')

plt.show()
