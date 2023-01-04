import numpy as np

a = np.array([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]])
flipped = np.flip(a)

def summ(a):
    np.flip(a)
    small = a[:2, :2]
    num = sum(small)
    ##num = sum(a[0[0]] + a[0[1]] + a[1[0]] + a[1[1]]) 
    return num


for i in a:
    max = summ(a)
    print (max)

