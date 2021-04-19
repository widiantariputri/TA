#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : new_main.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 17.04.2021
# Last Modified Date: 19.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

import numpy as np
import csv
import math

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

def make_criteria_arr(ava, ava_value):
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

def get_criteria_mat(arr, ava_value):
    identity_mat = np.identity(len(arr))
    end_for = int((math.pow(len(arr),2)-3)/2)
    for i in range(0, end_for):
        print('======================')
        _from = str(input('**choose criteria :'))
        print(f'other criteria to choose :')
        print([item for item in arr if _from not in item])
        _to = str(input('**terhadap criteria :'))
        print('**available value')
        for key, value in ava_value.items():
            print(key,value)
        _value = int(input('**Choose value:'))
        print('==SAVED==')
        criteria_arr = np.tile(np.array(arr), (3,1))
        identity_mat[arr.index(_from), arr.index(_to)] = _value
        identity_mat[arr.index(_to), arr.index(_from)] = float(1/_value)
    return identity_mat

def find_eigen(criteria):
    sum_of_col = np.sum(criteria, axis=0)
    eigen_vector = np.zeros_like(sum_of_col)
    for i in range(0, criteria.shape[0]):
        eigen_vector[i] = np.sum(np.divide(criteria[i], sum_of_col), axis=0)/criteria.shape[0]
    return eigen_vector, sum_of_col 

def calculate_lambda(eigen, sum_of_col):
    return np.sum(np.multiply(eigen, sum_of_col))

def find_ci_cr(l_max, criteria,r_index):
    ci = (l_max - len(criteria))/(len(criteria)-1) 
    cr = ci/r_index[len(criteria)] 
    return ci, cr


def main():
    # dependencies
    DATASET_DIR = 'DATASET/TEST.csv'
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
    sub_criteria = ['HB','BB','BC','JP','U','M','KC','DP','TK']

    # step 1 : reading dataset
    dataset = read_dataset(DATASET_DIR)
    # print(dataset)

    # step 2 : cleaning data
    cl_dataset = clean_dataset(dataset, __atr__)
    print(f'cleaned data : {cl_dataset}')

    # step 3 : making 3d identity criteria array
    criteria_arr = get_criteria_mat(ava_criteria, ava_value)
    print(criteria_arr)

    # step 4: finding eigen vector
    eigen_vector, sum_of_col = find_eigen(criteria_arr)
    print(f'eigen vector : \n{eigen_vector}\nsum of column: \n{sum_of_col}')
    lambda_max = calculate_lambda(eigen_vector, sum_of_col)
    print(f'Lambda max : {lambda_max}')
    CI,CR = find_ci_cr(lambda_max, ava_criteria,random_index)
    print(f'CI : {CI}, CR : {CR}')

    # step 5 : finding eigen vector sub-criteria matrix
    sub_eigen_mat = get_criteria_mat(sub_criteria,ava_value)
    print(f'sub criteria array:\n {sub_eigen_mat}')
    sub_eigen_vector, sub_sum = find_eigen(sub_eigen_mat)
    print(f'sub eigen vector : \n{sub_eigen_vector}\nsub sum of column: \n{sub_sum}')
    sub_lambda_max = calculate_lambda(sub_eigen_mat, sub_sum)
    print(f'Sub Lambda max : {sub_lambda_max}')
    sub_CI,sub_CR = find_ci_cr(sub_lambda_max, sub_criteria,random_index)
    print(f'Sub CI : {sub_CI}, Sub CR : {sub_CR}')

        

if __name__ == '__main__':
    main()


