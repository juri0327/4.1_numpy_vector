# -*- coding: utf-8 -*-

import numpy as np

def list2ndarray(input_list):
    return np.array(input_list)

def dist(x_array, y_array):
    return np.linalg.norm(x_array - y_array)

def extract(x_array):
    return x_array[1:-1]

def drop(x_array, idx):
    x_array[idx] = 0
    return x_array
