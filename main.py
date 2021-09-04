import numpy as np
import math
from SAW import *
# from ANP import *
from ayutANP import ANP
from itertools import combinations
from Kriteria import Kriteria, Alternative

# array untuk testing
from ArrayTest import M_predefined_array, C_predefined_array, A_predefined_array

'''

This is the driver code
A main portal to access all of the classes.


'''


def main():
    DDIR = 'DATASET/CSV.csv'

    # dictionary dari bobot dan subkriteria
    # call the ANP object
    M = Kriteria(['KT', 'BBB', 'HP'])
    C = Kriteria(['BP', 'BBC', 'PP', 'JS'])
    kriteria = (M, C)

    # ALTERNATIF
    A = Alternative()
    A.set_value(A_predefined_array)
    print(A.identitas)

    # MENGISI ARRAY JANGAN DIHAPUS
    # print('-----')
    # print('Mengisi sub kriteria M')
    # print('-----')

    # M.fill(C)

    # print('-----')
    # print('Mengisi sub kriteria M')
    # print('-----')
    # C.fill(M)

    # MENJALANKAN PROGRAM DENGAN ARRAY YANG UDH ADA
    M.set_value(M_predefined_array)
    C.set_value(C_predefined_array)

    # mulai ANP
    anp = ANP(measurable=M, capital=C, dataset=DDIR)
    anp.begin()

    '''

    anp = ANP(DDIR, SURVEY_DATA)

    gem = anp.get_gm()
    cluster_gm = anp.get_cluster_gm()

    matrix = anp.get_matrix()

    eigen_vector, anp_sum_col = anp.get_eigen(matrix)

    lambda_max = anp.get_lambda(eigen_vector, anp_sum_col)

    anp_ci, anp_cr = anp.get_ci_cr(lambda_max, matrix)

    eigen_alter = anp.get_eigen_alter()

    # the 'cluster' part-------

    cluster_mat = anp.get_cluster_matrix()

    cluster_eigen_vector, cluster_sum_col = anp.get_eigen(cluster_mat)

    cluster_lambda_max = anp.get_lambda(cluster_eigen_vector, cluster_sum_col)

    cluster_ci, cluster_cr = anp.get_ci_cr(cluster_lambda_max, cluster_mat)

    # unweighted matrix
    unweighted_mat = anp.get_unweighted_mat(matrix, eigen_alter)

    saw = SAW()
    hasil_saw = saw.get_hasil()
    '''


if __name__ == '__main__':
    main()
