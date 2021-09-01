'''
This file only include SAW
process.


'''
import numpy as np
import pandas as pd
class SAW:
    def __init__(self):
        # constant
        BOBOT_ALT = pd.read_csv('DATASET/TEST.csv')
        BOBOT_CRITERIA = [3,2,3,4,4,4,3]

        self.bobot_alt, self.bobot_raw = self.clean_data(BOBOT_ALT)

        self.cost_benefit = [1,1,1,0,1,1,0]
        min_max = self.get_min_max(self.cost_benefit,self.bobot_alt)
        norm_mat = self.normalize(self.bobot_alt, min_max, self.cost_benefit)
        self.total_weight = self.get_total_weight(BOBOT_CRITERIA,norm_mat)
        self.total_weight = self.total_weight.reshape(6,1)

        self.bobot_alt = np.append(self.bobot_raw, self.total_weight, axis=1)

        self.ranked_bobot = self.get_ranked_weight(self.bobot_alt)

    def get_hasil(self):
        obj = dict()
        label = ['Nama', 'Kode', 'Berat Campuran', 'Jumlah', 'Kecepatan Transaksi', 'Biaya', 'Ukuran', 'Berat', 'Harga (USD)', 'Total Harga']
        bobot = self.ranked_bobot

        for i in range(0, len(bobot)):
            obj[str(i)] = dict()
            for j in range(0, len(bobot[i])):
                obj[str(i)][label[j]] = bobot[i][j]
        return obj


    def clean_data(self, bobot):
        '''
            Cleaning dataset
            receive pandas dataframe as a parameter
        '''
        bobot =  np.array(bobot[bobot['JENIS'] == 'SILVER BRACELETS'])
        return bobot[:,2:], bobot


    def get_min_max(self,cost_benefit, bobot_alt):
        '''
        methods to get minimum and maximum valu each column
        takes cost_benefit and bobot_alt as parameter
        returning a single array
        '''
        min_max_arr = list()

        for i in range(len(cost_benefit)):
            if cost_benefit[i] == 0:
                # get minimum
                min_max_arr.append(min(bobot_alt[:,i]))
            else:
                min_max_arr.append(max(bobot_alt[:,i]))

        return min_max_arr


    def normalize(self, bobot, minmax, cost_ben):
        '''
        normalize matrix
        taking matrix and min max, cost_benefit  as parameter
        '''
        norm_mat = np.zeros_like(bobot)
        for i in range(len(cost_ben)):
            if cost_ben[i] == 1:
                norm_mat[:,i] = bobot[:,i]/minmax[i]
            else:
                mat = np.tile(minmax[i],len(bobot))
                norm_mat[:,i] = mat/bobot[:,i]

        return norm_mat


    def get_total_weight(self, criterias, norms):
        '''
        calculate the total weight
        '''
        return np.array([np.sum(np.multiply(np.array(criterias), norms[x,:])) for x in range(0, norms.shape[0])])


    def get_ranked_weight(self,bobot):
        '''
        rank in descending order
        '''
        return bobot[bobot[:,-1].argsort()][::-1]
