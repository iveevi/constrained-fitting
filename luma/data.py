#!/usr/bin/env python3

import numpy as np;

import matplotlib.pyplot as plt;

import random;

# Sorting data points
def sort_y(D, rev):
    Ds = {};

    for (x, y) in D:
        Ds[x] = y;

    S = sorted(Ds.items(), key = lambda x : x[1], reverse = rev);

    sD = [];

    for (x, y) in S:
        sD.append((x, y));

    return sD;

def sort_x(D, rev):
    Ds = {};

    for (x, y) in D:
        Ds[x] = y;

    S = sorted(Ds.items(), reverse = rev);

    sD = [];

    for (x, y) in S:
        sD.append((x, y));

    return sD;

# Set subtraction
def exclude(D, E):
    O = [];

    for i in D:
        bl = False;

        for S in E:
            if i in S:
                bl = True;

                break;

        if not bl:
            O.append(i);

    return O;
