import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

point = {"blue": [[2,4], [1,3], [2,3], [3,2], [2,1]],
        "red": [[5,6], [4,5], [4,6], [6,6], [5,4]]}

new_point = [3,3]

def euclidean_distance(p, q):
    np.sqrt(np.sum((np.array(p) - np.array(q)) ** 2))