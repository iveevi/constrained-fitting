#!/usr/bin/env python3

import random
import sys

import matplotlib.pyplot as plt
import numpy as np

from spike import *

sys.path.append('../modules')

from geometry import *
from graphing import *
from data import *

# Preprocessing
size = 25;
mx = 10;

D = uniform_data_set(size, 0, mx, mx/2, mx);

D_clh = convex_lower_hull(D);
D_cuh = convex_upper_hull(D);

clh_s = sort_y(D_clh, False);
cuh_s = sort_x(D_cuh, True);

# Required Sets
clh_min = [clh_s[0], clh_s[1]];
cuh_max = [cuh_s[0], cuh_s[1]];

# Set up the domain
t = np.arange(-1, mx, 0.01);

# Lower
lower, apex = spike_merged_lambda(clh_s[1], clh_s[0]);

plt.plot(t, lower(t));

# Upper
upper, apex = 0, 100

for i in cuh_s:
    for j in cuh_s:
        if i != j:
            tmp, tapex = spike_merged_lambda(i, j)

            over = True
            for k in cuh_s:
                if tmp(k[0]) < k[1]:
                    over = False

                    break

            if over:
                if upper == 0:
                    upper = tmp

                    apex = tapex
                elif apex > tapex:
                    upper = tmp

                    apex = tapex

#            plt.plot(t, tmp(t))

plt.plot(t, upper(t));

# Middle

mid = exclude(D, [D_clh, D_cuh]);

# H-Sifting with fulcrum at the left-most point
def h_sift(D, mu = 1):
    Ds = sort_x(D, False);

    O = [Ds[0]];

    latest = O[0];
    for i in Ds:
        if i[0] > latest[0] + mu:
            latest = i;

            O.append(i);

    return O;

mu = 1;

mid_sparse = h_sift(mid, mu);

eta = 1/np.exp(-mu * mu);

# plt.plot(t, spike_set(t, mid_sparse, eta), 'c');

# Average

plt.plot(t, (upper(t) + lower(t))/2);

# mid_weight = len(mid);

mid_weight = len(mid_sparse);

# plt.plot(t, (upper(t) + lower(t) + mid_weight * spike_set(t, mid_sparse, eta))/(2 +
#    mid_weight));

# Show graphs and data
plot(D, 'cx');

plot(clh_min, 'ro');
plot(cuh_max, 'go');

plot(mid, 'yo');
plot(mid_sparse, 'cv');

plot(D_clh, 'r-');
plot(D_cuh, 'g-');

plt.show();
