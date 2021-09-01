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
        self.geo_mean, self.cluster_data, self.cluster_gm = self.calc_geo_mean(survey_data)

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
                data.append(dt)

        for da in data:
            if not self.contain_zero(da):
                if da[0] == self.attr:
                    cl_data.append(da[0:])
        cl_data = np.array(cl_data)
        print(f'cl_data : {cl_data}')


        return cl_data


    def get_dataset(self):
        return self.dataset

    def calc_geo_mean(self,survey):
        survey_list = list()
        gm = dict()
        cluster_gm_dict = dict()
        with open(survey, 'r') as sur:
            survey_data = csv.reader(sur)
            for survey in survey_data:
                survey_list.append(survey)
        survey_list = np.array(survey_list)

        # splitting the data into cluster matrix
        cluster_data = survey_list[-3:]
        survey_list = survey_list[:-3]

        survey_label = survey_list[1:,0]
        cluster_label = cluster_data[:,0]

        survey_value = np.asfarray(survey_list[1:,1:], int)
        cluster_value = np.asfarray(cluster_data[:,1:], int)

        survey_gm = np.power(np.prod(survey_value, axis=1),(1./len(survey_value[0])))
        cluster_gm = np.power(np.prod(cluster_value, axis=1),(1./len(cluster_value[0])))

        for i in range(0, len(survey_label)):
            gm[survey_label[i]] = survey_gm[i]

        for i in range(0, len(cluster_label)):
            cluster_gm_dict[cluster_label[i]] = cluster_gm[i]

        return gm, cluster_data, cluster_gm_dict

    def get_gm(self):
        return self.geo_mean

    def get_cluster_gm(self):
        return self.cluster_gm


    def get_matrix(self):
        val_ = list()
        val_index = 0
        for key, value in self.geo_mean.items():
            val_.append(value)
        iden_mat = np.identity(7)


        for i in range(0, len(iden_mat)):
            for j in range(0, len(iden_mat[i])):
                if i!=j:
                    if i > j:
                        iden_mat[i][j] = 1/iden_mat[j][i]
                        # iden_mat[i][j] = 21
                    else :
                        iden_mat[i][j] = val_[((val_index%21))]
                        # iden_mat[i][j]= 25
                        val_index+=1
        return iden_mat

    def get_cluster_matrix(self):
        val_ = list()
        val_index = 0
        for key, value in self.cluster_gm.items():
            val_.append(value)
        iden_mat = np.identity(3)

        for i in range(0, len(iden_mat)):
            for j in range(0, len(iden_mat[i])):
                if i!=j:
                    if i > j:
                        iden_mat[i][j] = 1/iden_mat[j][i]
                        # iden_mat[i][j] = 21
                    else :
                        iden_mat[i][j] = val_[((val_index%21))]
                        # iden_mat[i][j]= 25
                        val_index+=1
        return iden_mat


    def get_eigen(self, mat):
        sum_of_col = np.sum(mat, axis=0)
        eigen_vector = np.zeros_like(sum_of_col)
        for i in range(0, mat.shape[0]):
            eigen_vector[i] = np.sum(np.divide(mat[i], sum_of_col), axis=0)/mat.shape[0]
        return eigen_vector, sum_of_col

    def get_eigen_alter(self):
        eigen_alter = list()
        trim_eigen = list()
        trim_dataset = self.dataset[:,2:].astype(float)


        for i in range(0, len(trim_dataset[0])):
            trim_trim = trim_dataset[:,i]
            trim_sum = np.sum(trim_trim)
            trim_eigen.append(trim_sum)
        # print(trim_eigen)
        trim_eigen = np.array(trim_eigen)

        for i in range(0, len(self.dataset)):
            head_ = self.dataset[i,2:].astype(float)
            eigen_alter.append(np.divide(head_, trim_eigen))

        return np.array(eigen_alter)

    def get_lambda(self, eigen, _sum):
        return np.sum(np.multiply(eigen, _sum))

    def get_ci_cr(self,l_max, mat):
        ci = (l_max - len(mat))/(len(mat)-1)
        cr = ci/self.random_index[len(mat)]
        return ci, cr

    def get_unweighted_mat(self,mat, alter):
        # buat matrix besar berukuran 14
        mat_size = len(mat)+len(alter)
        big_mat = np.zeros((mat_size, mat_size))
        print(f'matrix : {mat}\nalter : {alter}')
        print(f'array besar : {big_mat}')

        for i in range(0, len(big_mat)):
            for j in range(0, len(big_mat[i])):
                if i < (len(alter)):
                    if j < (len(mat)) :
                        big_mat[i][j] = 0
                    else:
                        big_mat[i][j] = 1/alter[j-(len(mat))][i]
                else:
                    if j < (len(mat)):
                        big_mat[i][j] = alter[i-(len(mat))][j-(len(mat))]


        print(big_mat)


