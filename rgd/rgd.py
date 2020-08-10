#!/usr/bin/env python3

import random
import sys

import matplotlib.pyplot as plt
import numpy as np

import autograd.numpy as anp

from autograd import elementwise_grad as egrad

sys.path.append('../modules')

from graphing import *
from data import *

# Creating the data set
size = 10
mx = 100

D = uniform_data_set(size, 0, mx, 0, mx)

t = np.arange(0, mx, 0.01)

# Model
a, b, c = 5.0, 3.0, 1.0

def f(x, a, b, c):
    return a * x * x + b * x + c

h, k = D[0]

def err_f(a, b, c):
    return k - f(h, a, b, c);

def loss_f(a, b, c):
    sm = 0

    for i in D:
        sm += (i[1] - f(i[0], a, b, c)) ** 2

    sm /= len(D)

    return sm

lfa = egrad(loss_f, 0)
lfb = egrad(loss_f, 1)
lfc = egrad(loss_f, 2)

print("Error: " + str(loss_f(a, b, c)))

dC = (lfa(a, b, c), lfb(a, b, c), lfc(a, b, c))

print("Gradient: " + str(dC))

# Plotting
fig, ax = plt.subplots(4, sharex = True)

ax[3].plot(t, f(t, a, b, c), 'b')

gamma = 0.000003

for i in range(0, 100):
    dC = (lfa(a, b, c), lfb(a, b, c), lfc(a, b, c))

    sdC = [gamma * x for x in dC]

    print("\t" + str(sdC))

    a, b, c = np.subtract((a, b, c), sdC)

ax[3].plot(t, f(t, a, b, c), 'r')

ax[3].plot(h, k, 'go')

plot(D, 'cx')


ax[0].plot(t, err_f(t, b, c));
ax[0].plot(t, lfa(t, b, c));

ax[1].plot(t, err_f(a, t, c));
ax[1].plot(t, lfb(a, t, c));

ax[2].plot(t, err_f(a, b, t));
ax[2].plot(t, lfc(a, b, t));

plt.show()
