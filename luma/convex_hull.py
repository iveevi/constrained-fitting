#!/usr/bin/env python3

import numpy as np;

import matplotlib.pyplot as plt;

import random;

from graphing import *

# Convex Hulls
def convex_lower_hull(D):
    clh = [];

    # Find left-most point
    mx, my = D[0];

    for i in D:
        if i[0] < mx:
            mx, my = i;

    # Start the clh
    clh.append((mx, my));

    # Add more points
    px, py = mx, my;

    while True:
        x, y = D[0][0], D[0][1];

        if (px, py) == (D[0][0], D[0][1]):
            mdx, mdy = (px - D[1][0]), (py - D[1][1]);

            x, y = D[1][0], D[1][1];
        else:
            mdx, mdy = (px - D[0][0]), (py - D[0][1]);

        found = 0;

        for i in D:
            if i[0] <= px:
                continue;

            found += 1;

            dx, dy = (px - i[0]), (py - i[1]);

            if dy * mdx < mdy * dx:
                mdx, mdy = dx, dy;

                x, y = i[0], i[1];

        if found > 0:
            px, py = x, y;

            clh.append((x, y));
        else:
            break;

    return clh;

def convex_upper_hull(D):
    cuh = [];

    # Find left-most point
    mx, my = D[0];

    for i in D:
        if i[0] < mx:
            mx, my = i;

    # print(mx, my);

    # Start the clh
    cuh.append((mx, my));

    # Add more points
    px, py = mx, my;

    while True:
        x, y = D[0][0], D[0][1];

        if (px, py) == (D[0][0], D[0][1]):
            mdx, mdy = (px - D[1][0]), (py - D[1][1]);

            x, y = D[1][0], D[1][1];
        else:
            mdx, mdy = (px - D[0][0]), (py - D[0][1]);

        # print("(PX, PY): " + str((px, py)));

        found = 0;

        for i in D:
            if i[0] <= px:
                continue;

            found += 1;

            dx, dy = (px - i[0]), (py - i[1]);

            if dy * mdx > mdy * dx:
                mdx, mdy = dx, dy;

                x, y = i[0], i[1];

        if found > 0:
            px, py = x, y;

            cuh.append((x, y));
        else:
            break;

    return cuh;
