'''
 orak - orek

'''
import numpy as np


def main():
    arr = np.array(([[1,7,0.5],[0.14285714,1,0.2],[2,5,1]]))
    sum_of_col = np.array([3.14285714, 13, 1.7])
    eigen_vector = np.zeros_like(sum_of_col)
    
    for i in range(0, arr.shape[0]):
        eigen_vector[i] = np.sum(np.divide(arr[i], sum_of_col), axis=0)/3

    print(eigen_vector)



if __name__ == '__main__':
    main()
