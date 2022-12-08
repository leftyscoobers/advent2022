# Given grid of "tree heights" from 0 to 9
# Prob 1 find trees that are visible from the edges

import numpy as np

lines = [list(l.strip()) for l in open('tmp.txt', 'r').readlines()]
forest_list = []
for r in lines:
    forest_list.append([int(t) for t in r])

forest = np.array(forest_list)

