import numpy as np
import pandas as pd


class ANP(object):
    def __init__(self, measurable,
                 capital, alternative, criteria_range, dataset):
        self.M = measurable
        self.C = capital
        self.A = alternative
        self.range = criteria_range
        self.dataset = dataset

    def begin(self):
        # tempat menampung eigen vector yang terbentuk
        self.kri_eigen_vector = self.get_eigen(self.range)
        self.kri_all = self.get_eigen_arr(self.kri_eigen_vector)
        print(self.kri_all)

    def get_eigen(self, ran):
        eigen_list = list()
        for r in ran:
            # mencari jumlah kolom dan baris
            sum_x, sum_y = self.sum_of_axis(r)
            # normalisasi array berdasarkan
            # jumlah kolom dan baris
            r = self.normalize_with(sum_x, sum_y, r)
            eigen_list.append(r.sum(axis=1)/len(r.sum(axis=1)))

        return eigen_list

    def sum_of_axis(self, arr: np.array):
        '''
        Method kelas untuk menghitung jumlah
        baris dan jumlah kolom pada np.array.

        Return : sum_x, sum_y
        sum_x : jumlah pd baris
        sum_y : jumlah pd kolom
        '''
        return np.sum(arr, axis=1), np.sum(arr, axis=0)

    def normalize_with(self, x, y, arr):
        '''
        Normalisasi array dengan nilai custom x, y dan array
        Return : array yang termodifikasi
        '''
        arr[1, :] = arr[1, :]/x[::-1]
        arr[0, :] = arr[0, :]/y
        return arr

    def get_eigen_arr(self, vector):
        '''
        Membuat matriks eigen untuk sebuah array
        Bisa untuk kategori dan sub kategori
        Return : array
        '''

        zero_identity = np.zeros((len(vector), len(vector)))
        zero_identity[0][2] = vector[0][0]
        zero_identity[1][2] = vector[0][1]
        zero_identity[0][1] = vector[1][0]
        zero_identity[2][1] = vector[1][1]
        zero_identity[1][0] = vector[2][0]
        zero_identity[2][0] = vector[2][1]

        return zero_identity
