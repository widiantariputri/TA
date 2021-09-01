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
    SURVEY_DATA = 'DATASET/ANOTHER_RESPONDEN.csv'

    anp = ANP(DDIR,SURVEY_DATA)

    gem = anp.get_gm()
    cluster_gm = anp.get_cluster_gm()

    matrix = anp.get_matrix()

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)

    anp_ci, anp_cr = anp.get_ci_cr( lambda_max, matrix)

    eigen_alter = anp.get_eigen_alter()



    # the 'cluster' part-------

    cluster_mat = anp.get_cluster_matrix()

    cluster_eigen_vector, cluster_sum_col = anp.get_eigen(cluster_mat)

    cluster_lambda_max = anp.get_lambda(cluster_eigen_vector, cluster_sum_col)

    cluster_ci, cluster_cr = anp.get_ci_cr( cluster_lambda_max, cluster_mat)

    # unweighted matrix
    unweighted_mat = anp.get_unweighted_mat(matrix,eigen_alter)


    saw = SAW()
    hasil_saw = saw.get_hasil()
    print(hasil_saw)







if __name__ == '__main__':
    main()
