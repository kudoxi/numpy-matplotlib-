import numpy as np

a = np.arange(1,10).reshape(3,3)
print(a,type(a))
m = np.matrix(a,copy=True)
m2 = np.matrix(a,copy=False)
a[0,0] = 999
print(m,type(m))
print(m2,type(m2))

m3 = np.mat('12 34 45;24 54 23')
print(m3,type(m3))


#矩阵的乘法
a = np.arange(1,7).reshape(2,3)
b = a.copy()
#对应位置相乘
print(a*b)
a = np.mat(a)
b = np.mat(b).T
#1*1+2*2+3*3   1*4+2*5+3*6     14  32
#4*1+5*2*6*3   4*4+5*5+6*6     32  77
print(a*b)
#矩阵的逆
m = np.mat('1 2 3;4 4 4;2 4 3')
print(m.I)
#检验是否真的可逆
print(m.dot(m.I))

#非方正的逆矩阵（广义逆矩阵）
m = np.mat('1 2 3;4 4 4')
print(m.I)
print(m.dot(m.I))


#解方程
#大人小孩乘车去Ａ地，大人一人３．２，小孩一人３块，
# 回来的时候乘车大人一人３．６，小孩一人３．５
#求大人和小孩各多少人
#方法一
prices = np.mat('3 3.2;3.5 3.6')
totals = np.mat('118.4;135.2')
x = np.linalg.lstsq(prices,totals)[0]
print("小孩：",x[0],"大人：",x[1])

#方法二
persons = prices.I * totals
print(persons)



#斐波那契数列
A = np.mat('1 1;1 0')
#求第n个数
def feibonaqi(A,n):
    return A**n

print(feibonaqi(A,3)[0,0])