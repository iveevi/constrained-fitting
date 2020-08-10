#!/usr/bin/env python3

import numpy as np;

import matplotlib.pyplot as plt;

import random;

#####################################
#                                   #
# Kernel is assumed to be exp(-x^2) #
#                                   #
#####################################

# Spike with apex and acuteness factor
def spike(eta, h, k, x):
    return k * np.exp(-eta * (x - h) * (x - h));

# Spike (Lambda) with apex and acuteness factor
def spike_lambda(eta, h, k):
    return lambda a : k * np.exp(-eta * (a - h) * (a - h));

# Spike over set with optional acuteness factor
def spike_set(x, D, eta = 1):
    sm = 0;

    for (h, k) in D:
        sm += k * np.exp(-eta * (x - h) * (x - h));

    return sm;

# Spike (Lambda) of merged spikes with auto acuteness
def spike_merged_lambda(p, q, bnd, over):
    a, b = p;
    c, d = q;

    if a - c < 1:
        eta = abs(a - c)/100;
    else:
        eta = 1/np.exp(a - c);

    p = (a - c) * (a - c);
    l = np.log(d/b);

    A = (eta * p * p + 2 * p * l + l * l / eta)/(4 * p);

    klog = A + np.log(b);

    # Determining the correct h
    sign = 0;

    tmp = b * np.exp(-eta * (c - a) * (c - a));
    if c > a:
        if d > tmp:
            sign = 1;
        else:
            sign = -1;
    else:
        if d > tmp:
            sign = -1;
        else:
            sign = 1;

    h = a + sign * np.sqrt((klog - np.log(b))/eta);

    return lambda x : np.exp(klog - eta * (x - h) * (x - h)), klog
