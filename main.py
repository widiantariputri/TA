import csv
import numpy as np

def baca_data(dt):
    data = list()
    with open(dt) as csv_file:
        dt_reader = csv.reader(csv_file, delimiter=",")
        for dt in dt_reader:
            # print(dt)
            data.append(dt)
    return data

def contain_zero(sub):
    zero_count = 0
    for el in sub:
        if el == '':
            zero_count+=1
    if zero_count > 0:
        return True
    else:
        return False
def data_cleaning(data):
    cl_data = list()
    
    for da in data:
        if not contain_zero(da):
            if da[3] == 'SILVER BRACELETS':
                cl_data.append(da[1:])
    
    # print(cl_data)
    return cl_data

def find_eigen_vector(_arr):

    # jumlahkan data per kolom
    _w =  np.sum(_arr, axis = 0)
    # ev -> eigen vector
    ev = list()
    for i in range(0, len(_arr)):
        _res = 0
        _list = list()
        for j in range(0, len(_arr[i])):
            _res += _arr[i][j] / _w[j]
        _list.append(_res/len(_w))
        ev.append(_list)
    
    return np.array(ev), _w
    

def find_kriteria(_ktr):
    _arr = np.array([[1, _ktr], [float(1/_ktr), 1]])

    return _arr


def main():
    random_index = {
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
    dataset = "DATASET/TEST.CSV"
    # 1.baca data
    data = baca_data(dataset)
    # print(data)

    # 2. data cleaning
    data_cl = data_cleaning(data)
    

    # rubah ke array
    data_cl = np.array(data_cl)
    # print(data_cl)
    _kriteria = int(input('Pilih tingkat kriteria : '))
    arr_ktr = find_kriteria(_kriteria)

    # cari eigen vector
    eig_vector, _we = find_eigen_vector(arr_ktr)

    # gabung array jadi 1
    arr_ktr = np.append(arr_ktr, eig_vector, axis=1)
    # print(arr_ktr)

    # cari lambda max
    lambda_max = 0
    for i in range(0, len(_we)):
        lambda_max+=_we[i]*eig_vector[i][0]

    # cari ci
    ci = (lambda_max-len(arr_ktr))/(len(arr_ktr)-1)
    
    # cari cr
    ri = 0
    for random in random_index:
        if random == len(arr_ktr):
            ri = random_index[random]
    
    cr = 0
    if ri == 0:
        cr = 0
    else:
        cr = ci/ri
      

if __name__=='__main__':
    main()