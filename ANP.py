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
    def __init__(self, ddir, survey_data):
        self.criteria_value = {
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
        self.attr = 'SILVER BRACELETS'
        self.dataset = self.readCleanData(ddir)
        self.geo_mean = self.calc_geo_mean(survey_data)



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
                if da[2] == self.attr:
                    cl_data.append(da[1:])
        cl_data = np.array(cl_data)
        return cl_data


    def get_dataset(self):
        return self.dataset

    def calc_geo_mean(self,survey):
        survey_list = list()
        gm = dict()
        with open(survey, 'r') as sur:
            survey_data = csv.reader(sur)
            for survey in survey_data:
                survey_list.append(survey)
        survey_list = np.array(survey_list)

        survey_label = survey_list[1:,0]
        survey_value = np.asfarray(survey_list[1:,1:], int)
        survey_gm = np.sqrt(np.prod(survey_value, axis=1)/len(survey_value[0]))

        for i in range(0, len(survey_label)):
            gm[survey_label[i]] = survey_gm[i]
        
        return gm

    def get_gm(self):
        return self.geo_mean


    def get_matrix(self):
        val_ = list()
        for key, value in self.geo_mean.items():
            print(key, value)
            val_.append(value)
        iden_mat = np.identity(7)
        
        for i in range(0, len(iden_mat)):
            for j in range(0, len(iden_mat[i])):
                if i!=j:
                    if i > j:
                        iden_mat[i][j] = 1/iden_mat[0][j+1]
                        # iden_mat[i][j] = 21
                    else :
                        iden_mat[i][j] = val_[((j%21)-1)]
                        # iden_mat[i][j]= 25

        return iden_mat


