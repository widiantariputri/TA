#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ANP.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 21.04.2021
# Last Modified Date: 21.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>

'''
This file only include ANP
process.


'''
import csv
import math
import numpy as np

class ANP:
    def __init__(self):
        self.ava_value = {
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
        self.random_index = {
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
        self.__atr__ = 'SILVER BRACELETS'
        self.ava_criteria = ['KB', 'P', 'I']
        self.sub_criteria = ['HB','BB','BC','JP','U','M','KC','DP','TK']



    def contain_zero(self,sub):
        zero_count = 0
        for el in sub:
            if el == '':
                zero_count+=1
        if zero_count > 0:
            return True
        else:
            return False

    def readCleanData(self,ddir):
        data = list()
        cl_data = list()
        with open(ddir, 'r') as csv_file:
            dt_reader = csv.reader(csv_file, delimiter=",")
            for dt in dt_reader:
                # print(dt)
                data.append(dt)
                
        for da in data:
            if not self.contain_zero(da):
                if da[2] == 'SILVER BRACELETS':
                    cl_data.append(da[1:])
        return np.array(cl_data)

