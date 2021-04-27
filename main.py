#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : main.py
# Author            : Teguh Satya <teguhsatyadhr@gmail.com>
# Date              : 21.04.2021
# Last Modified Date: 21.04.2021
# Last Modified By  : Teguh Satya <teguhsatyadhr@gmail.com>
import numpy as np
import math
from SAW import *
from ANP import *

'''

This is the driver code
A main portal to access all of the classes.


'''

def main():
    DDIR = 'DATASET/TEST.csv'
    SURVEY_DATA = 'DATASET/RESPONDEN.csv'
    anp = ANP(DDIR,SURVEY_DATA)

    dataset = anp.get_dataset()
    gem = anp.get_gm()
    matrix = anp.get_matrix()

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)
    print(f'eigen vector :\n {eigen_vector}\nsum = {anp_sum_col}')

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)
    print(f'lambda max = {lambda_max}')

    anp_ci, anp_cr = anp.get_ci_cr( lambda_max, matrix)
    print(f'CI : {anp_ci}, CR: {anp_cr}')


    
    # saw = SAW()




if __name__ == '__main__':
    main()
