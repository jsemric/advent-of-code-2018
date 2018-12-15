#!/usr/bin/env python

import sys
import numpy as np
import itertools

def manhatan(a,b):
    return int(np.abs(a[0]-b[0]) + np.abs(a[1]-b[1]))

def assign(a, coords):
    dists = [(v,manhatan(a,k)) for k,v in coords.items()]
    min_dist = min(dists,key=lambda x: x[1])
    min_dists = [x for x in dists if x[1] == min_dist[1]]
    assert len(min_dists) > 0

    if len(min_dists) == 1:
        return min_dists[0][0]

    return -1

def part1(l, max_x, max_y, coords):
    dcoords = {}

    for i,(x,y) in enumerate(coords):
        l[x][y] = i + 1
        dcoords[(x,y)] = i + 1

    coords_vals = set(dcoords.values())
    for (i,j) in itertools.product(range(max_x+1),range(max_y+1)):
        p = int(assign((i,j), dcoords))
        l[i][j] = p

        if i == 0 or j == 0 or i == max_x or j == max_y:
            coords_vals.discard(p)

    area = max(l[l == i].size for i in coords_vals)
    return area

def  main():
    coords = []
    for i in sys.stdin:
        x,y = i.split(', ')
        coords.append((int(x),int(y)))

    min_x = min(coords, key=lambda x: x[0])[0]
    min_y = min(coords, key=lambda x: x[1])[1]

    coords = [(x-min_x,y-min_y) for (x,y) in coords]
    max_x = max(coords, key=lambda x: x[0])[0]
    max_y = max(coords, key=lambda x: x[1])[1]

    l = np.zeros((max_x+1, max_y+1),dtype=int)

    area = part1(l, max_x, max_y, coords)
    print('First answer:', area)

    for (i,j) in itertools.product(range(max_x+1),range(max_y+1)):
        l[i][j] = sum(manhatan((i,j),c) for c in coords)

    print('Second answer:', l[l < 10000].size)

if __name__ == '__main__':
    main()
