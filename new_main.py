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
    identity_mat = np.identity(3)
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
        print(_from, _to, _value, ava_value[_value])


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
        



    








if __name__ == '__main__':
    main()


