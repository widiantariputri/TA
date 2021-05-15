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

    gem = anp.get_gm()
    cluster_gm = anp.get_cluster_gm()

    matrix = anp.get_matrix()
    print(f'matrix : {matrix}')

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)
    print(f'eigen vector :\n {eigen_vector}\nsum = {anp_sum_col}')

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)
    print(f'lambda max = {lambda_max}')

    anp_ci, anp_cr = anp.get_ci_cr( lambda_max, matrix)
    print(f'CI : {anp_ci}, CR: {anp_cr}')

    eigen_alter = anp.get_eigen_alter()
    print(f'eigen alternatif : {eigen_alter}')

    

    # the 'cluster' part-------
    
    cluster_mat = anp.get_cluster_matrix()
    print(f'cluster_mat : {cluster_mat}')

    cluster_eigen_vector, cluster_sum_col = anp.get_eigen(cluster_mat)
    print(f'cluster eigen vector :\n {cluster_eigen_vector}\ncluster sum = {cluster_sum_col}')

    cluster_lambda_max = anp.get_lambda(cluster_eigen_vector, cluster_sum_col)
    print(f'cluster lambda max = {cluster_lambda_max}')

    cluster_ci, cluster_cr = anp.get_ci_cr( cluster_lambda_max, cluster_mat)
    print(f'CI : {cluster_ci}, CR: {cluster_cr}')

    # cluster_eigen_alter = anp.get_eigen_alter()
    # print(f'eigen alternatif : {eigen_alter}')


    
    # saw = SAW()




if __name__ == '__main__':
    main()
