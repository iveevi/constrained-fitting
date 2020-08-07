#!/usr/bin/env python3

import numpy as np;

import matplotlib.pyplot as plt;

import random;

def random_data_set(n):
    D = [];

    for i in range(0, n):
        x, y = random.random(), random.random();

        D.append((x, y));

    return D;

def uniform_data_set(n, ax, bx, ay, by):
    D = [];

    for i in range(0, n):
        x, y = random.uniform(ax, bx), random.uniform(ay, by);

        D.append((x, y));

    return D;

def plot(D, opt, label = False):
    Dx = [i[0] for i in D];
    Dy = [i[1] for i in D];

    plt.plot(Dx, Dy, opt);

    if label:
        for i in range(0, len(Dx)):
            plt.annotate((Dx[i], Dy[i]), (Dx[i], Dy[i]));
