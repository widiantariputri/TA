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
    dataset = ANP().readCleanData(DDIR)
    print(dataset)
    # saw = SAW()




if __name__ == '__main__':
    main()
