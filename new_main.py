#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : new_main.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 17.04.2021
# Last Modified Date: 17.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

import numpy as np
import csv

def read_dataset(ddir):
    dataset = list()
    with open(ddir, 'r') as _file:
        csv_reader = csv.reader(_file)
        for item in csv_reader:
            dataset.append(item)
    return dataset

def clean_dataset(datas, atr):
    cleaned_data = list()
    for data in datas:
        # print(f'checking {data} contain {atr} : {atr in data}')
        if atr in data:
            cleaned_data.append(data)
    return np.array(cleaned_data)

def make_criteria_arr(ava):
    ava_value = {
            1 : 'Sama Penting',
            2 : 'Nilai Tengah',
            3 : 'Sedikit Lebih Penting',
            4 : 'Nilai Tengah',
            5 : 'Lebih Penting',
            6 : 'Nilai Tengah',
            7 : 'Sangat Penting',
            8 : 'Nilai Tengah',
            9 : 'Mutlak Penting'
            }

    already_selected_criteria = list()
    identity_mat = np.identity(3)
    for i in range(0, len(ava)):
        print('======================')
        _from = str(input('**choose criteria :'))
        print(f'other criteria to choose :')
        print([item for item in ava if _from not in item])
        _to = str(input('**terhadap criteria :'))
        print('**available value')
        for key, value in ava_value.items():
            print(key,value)
        _value = int(input('**Choose value:'))
        print('==SAVED==')
        criteria_arr = np.tile(np.array(ava), (3,1))
        identity_mat[ava.index(_from), ava.index(_to)] = _value
        identity_mat[ava.index(_to), ava.index(_from)] = float(1/_value)
        print(identity_mat)
    return identity_mat

def find_eigen(criteria):
    sum_of_col = np.sum(criteria, axis=0)
    eigen_vector = np.zeros_like(sum_of_col)
    for i in range(0, criteria.shape[0]):
        eigen_vector[i] = np.sum(np.divide(criteria[i], sum_of_col), axis=0)/criteria.shape[0]
    return eigen_vector, sum_of_col 



def main():
    # dependencies
    DATASET_DIR = 'DATASET/TEST.csv'
    __atr__ = 'SILVER BRACELETS'
    random_index = {
        1 : 0,
        2 : 0,
        3 : 0.58,
        4 : 0.9,
        5 : 1.12,
        6 : 1.24,
        7 : 1.32,
        8 : 1.21,
        9 : 1.45,
        10 : 1.49
    }
    # available criteria made by system
    ava_criteria = ['KB', 'P', 'I']


    # step 1 : reading dataset
    dataset = read_dataset(DATASET_DIR)
    # print(dataset)

    # step 2 : cleaning data
    cl_dataset = clean_dataset(dataset, __atr__)
    print(f'cleaned data : {cl_dataset}')

    # step 3 : making 3d identity criteria array
    criteria_arr = make_criteria_arr(ava_criteria)
    print(criteria_arr)

    # step 4: finding eigen vector
    eigen_vector, sum_of_col = find_eigen(criteria_arr)
    lambda_max = np.sum(np.multiply(eigen_vector, sum_of_col))

    print(lambda_max)

        



    








if __name__ == '__main__':
    main()


