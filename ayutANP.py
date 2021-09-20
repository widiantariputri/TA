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
        self.atribut_eigen = self.get_atr_eigen(self.dataset).fillna(0)
        # self.atribut_transpose = np.array(self.atribut_eigen.T)
        self.atribut_transpose = self.atribut_eigen.transpose()

        print('matrix eigen MCA')
        print(self.kri_all)
        print('sub-kriteria')
        print(self.subkriteria_eigen)
        print('alternatif')
        print(self.atribut_eigen)
        print('alternatif transpose')
        print(self.atribut_transpose)

        self.sub_CM = self.get_sub_eigen([self.M])
        self.sub_MC = self.get_sub_eigen([self.C])
        self.atribut_M = self.atribut_eigen[['KT Eigen Vector', 'BBB Eigen Vector', 'HP Eigen Vector']]
        self.atribut_C = self.atribut_eigen[['BP Eigen Vector', 'BBC Eigen Vector', 'PP Eigen Vector', 'JS Eigen Vector']]
        self.atribut_transpose_M = self.atribut_transpose.iloc[:4]
        self.atribut_transpose_C = self.atribut_transpose.iloc[4:]

        self.w_sub_CM = self.get_weighted(self.sub_CM, self.kri_all[1][0])
        self.w_sub_MC = self.get_weighted(self.sub_MC, self.kri_all[0][1])
        self.w_atribut_M = self.get_weighted(self.atribut_M, self.kri_all[2][0])
        self.w_atribut_C = self.get_weighted(self.atribut_C, self.kri_all[2][1])
        self.w_atribut_TM = self.get_weighted(self.atribut_transpose_M, self.kri_all[0][2])
        self.w_atribut_TC = self.get_weighted(self.atribut_transpose_C, self.kri_all[1][2])
        
        print(self.w_sub_CM)
        print(self.w_sub_MC)
        print(self.w_atribut_C)
        print(self.w_atribut_M)
        print(self.w_atribut_TC)
        print(self.w_atribut_TM)

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

    def read_dataset(self, data):
        '''
        Untuk read data menggunakan pandas
        Params : Lokasi data
        Return : Dataframe
        '''
        dataset = pd.read_csv(data)
        dataset = dataset[dataset['JENIS'] == 'SILVER BRACELETS']

        # cleaning process belum dilakukan
        return dataset

    def get_atr_eigen(self, data: pd.DataFrame) -> pd.DataFrame:
        '''
        Membuat eigen dari atribut
        Params : Data : Dataset
        Return : Dataframe
        '''
        dataset = self.read_dataset(data)
        eigen_atr = pd.DataFrame()

        # Supaya engga memasukkan kode
        dataset_columns = dataset.columns[2:]

        for col in dataset_columns:
            col_sum = dataset[col].sum()
            eigen_atr[f'{col} Eigen Vector'] = dataset[col] / col_sum

        return eigen_atr

    def get_weighted(self, sub_matrix, scalar):
        if(type(sub_matrix) != np.ndarray):
            sub_matrix = np.array(sub_matrix)
        weighted = sub_matrix * scalar
        return weighted
