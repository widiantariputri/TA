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
        print(f'checking {data} contain {atr} : {atr in data}')
        if atr in data:
            cleaned_data.append(data)
    return np.array(cleaned_data)
            


def main():
    DATASET_DIR = 'DATASET/TEST.csv'
    __atr__ = 'SILVER BRACELETS'

    # step 1 : reading dataset
    dataset = read_dataset(DATASET_DIR)
    print(dataset)

    # step 2 : cleaning data
    cl_dataset = clean_dataset(dataset, __atr__)
    print(f'cleaned data : {cl_dataset}')






if __name__ == '__main__':
    main()


