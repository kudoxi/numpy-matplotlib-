import numpy as np


pros = np.array(['Apple','Huawei','Mi','OPPO','VIVO'])
pric = np.array([8888,4999,2999,3999,3999])
vols = np.array([100,200,70,80,90])
print(np.msort(vols))
#联合间接排序
indies = np.lexsort((vols,pric))
print(pros[indies])
#插入排序
a = np.array([1,2,3,4,5,7,8,10])
b = np.array([9,6])
indies = np.searchsorted(a,b)
print(indies)#应该插入的数组下标
c = np.insert(a,indies,b)
print(c)#[ 1  2  3  4  5  6  7  8  9 10]