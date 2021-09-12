import numpy as np
import math
from SAW import *
# from ANP import *
from ayutANP import ANP
from itertools import combinations
from Kriteria import Kriteria, Alternative

# array untuk testing
from ArrayTest import M_predefined_array, C_predefined_array, Criteria_range_value

'''

This is the driver code
A main portal to access all of the classes.


'''


def assign_criteria_range(fr, to, val, arr):
    '''
    Assigning value to criteria
    fr = from
    to = to
    val = value
    arr = criteria identity array
    '''

    if fr == 'm' and to == 'c':
        arr[0][0][1] = val
        arr[0][1][0] = 1/val

    elif fr == 'c' and to == 'm':
        arr[0][0][1] = 1/val
        arr[0][1][0] = val

    elif fr == 'm' and to == 'a':
        arr[1][0][1] = val
        arr[1][1][0] = 1/val

    elif fr == 'a' and to == 'm':
        arr[1][0][1] = 1/val
        arr[1][1][0] = val

    elif fr == 'c' and to == 'a':
        arr[2][0][1] = val
        arr[2][1][0] = 1/val

    elif fr == 'a' and to == 'c':
        arr[2][0][1] = 1/val
        arr[2][1][0] = val
    else:
        print('Not found')

    return arr


def main():
    DDIR = 'DATASET/TEST.csv'

    # dictionary dari bobot dan subkriteria
    # call the ANP object
    M = Kriteria(['KT', 'BBB', 'HP'])
    C = Kriteria(['BP', 'BBC', 'PP', 'JS'])

    # ALTERNATIF
    A = Alternative()

    # Membuat relasi antara M dengan C atau M dengan A
    # JANGAN DIHAPUS INI UDH SELESAI NGISI NILAI
    # KRITERIA = ('M', 'C', 'A')
    # KRITERIA_VALUE = [np.identity(2) for i in range(0, len(KRITERIA))]

    # for i in range(0, len(KRITERIA)):
    #     print(f'Opsi yang tesedia : {KRITERIA}')
    #     from_criteria = str(input('Ketik kriteria : ')).lower()
    #     to_criteria = str(input('Terhadap kriteria : ')).lower()
    #     range_value = float(input('Nilai kriteria : '))
    #     KRITERIA_VALUE = assign_criteria_range(from_criteria, to_criteria,
    #                                            range_value, KRITERIA_VALUE)

    # print(KRITERIA_VALUE)
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
    anp = ANP(
        measurable=M,
        capital=C,
        alternative=A,
        criteria_range=Criteria_range_value,
        dataset=DDIR

    )
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
