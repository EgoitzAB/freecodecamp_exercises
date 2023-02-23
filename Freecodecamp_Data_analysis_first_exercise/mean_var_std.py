#!/usr/bin/python3
import numpy as np

def calculate(list_of_numbers):
    calculation_dictionary = {}
    if len(list_of_numbers) != 9:
        raise ValueError ("List must contain nine numbers.")
    else:
        array = np.array(list_of_numbers).reshape(3,3)
    variance_1 = list(np.var(array, axis=0))
    variance_2 = list(np.var(array, axis=1))
    variance_flattened = np.var(array).tolist()
    mean_1 = np.mean(array, axis=0).tolist()
    mean_2 = np.mean(array, axis=1).tolist()
    mean_flattened = np.mean(array).tolist()
    deviation_1 = np.std(array, axis = 0, dtype = np.float64).tolist()
    deviation_2 = np.std(array, axis = 1, dtype = np.float64).tolist()
    deviation_flattened = np.std(array, dtype = np.float64).tolist()
    max_1 = np.max(array, axis=0).tolist()
    max_2 = np.max(array, axis=1).tolist()
    max_flattened = np.max(array).tolist()
    min_1 = np.min(array, axis=0).tolist()
    min_2 = np.min(array, axis=1).tolist()
    min_flattened = np.min(array).tolist()
    sum_1 = np.sum(array, axis=0).tolist()
    sum_2 = np.sum(array, axis=1).tolist()
    sum_flattened = np.sum(array).tolist()

    calculation_dictionary['mean']= mean_1, mean_2, mean_flattened
    calculation_dictionary['variance']= variance_1, variance_2, variance_flattened
    calculation_dictionary['standard deviation']= deviation_1, deviation_2, deviation_flattened
    calculation_dictionary['max']= max_1, max_2, max_flattened
    calculation_dictionary['min']= min_1, min_2, min_flattened
    calculation_dictionary['sum']= sum_1, sum_2, sum_flattened
    return calculation_dictionary

