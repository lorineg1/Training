import numpy as np

a = np.array([[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]])
checker = 0

def summ(a):
    small = a[:2, :2]
    num = sum(sum(small)) 
    return num

for i in range(1,16):
    max = summ(a)
    a = np.flip(a)
    if (max > checker) :
        checker = max

print(checker)
    

