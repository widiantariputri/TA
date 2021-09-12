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
        '''
        Memulai semua operasi ANP
        Return : ANP matriks

        '''
        # tempat menampung eigen vector yang terbentuk
        self.kri_eigen_vector = self.get_eigen(self.range)
        self.kri_all = self.get_eigen_arr(self.kri_eigen_vector)
        self.subkriteria_eigen = self.get_sub_eigen((self.M, self.C))
        print(self.subkriteria_eigen)

    def get_sub_eigen(self, subs) -> list:
        '''
        Mencari nilai eigen untuk sub kriteria masing2 kriteria
        Params : Tuple dari semua kriteria
        Return : list dari semua subeigen
        '''
        sub_eigen_list = list()
        for sub in subs:
            for element in sub.kriteria_all:
                sum_x, sum_y = self.sum_of_axis(element.value)
                element.value = self.normalize_with(
                    sum_x, sum_y, d_arr=element.value)
                sub_eigen_list.append(
                    element.value.sum(axis=1)/len(element.value))
        return sub_eigen_list

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

    def normalize_with(self, x: np.array, y: np.array, arr=None, d_arr=None):
        '''
        Normalisasi array dengan nilai custom x, y dan array
        Return : array yang termodifikasi
        Param :
        x = sum of x axis
        y = sim of y axis
        arr = one dimensional array
        d_arr = multidimensional array
        '''
        if d_arr is None:
            arr[1, :] = arr[1, :]/x[::-1]
            arr[0, :] = arr[0, :]/y
            return arr

        else:
            d_arr = d_arr/y
            return d_arr

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
