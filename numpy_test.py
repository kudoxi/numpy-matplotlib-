import numpy as np

a = np.array(range(1,6))
print(a,a.shape)
a = a *3
print(a)

b = np.arange(0,10,2)
print(b)

c = np.zeros(10,dtype='int32')
print(c)

d = np.ones(10,dtype='bool')
print(d)

e = np.full(10,3.14)
print(e)

a2 = np.array([[1,2,3],[4,5,6]],dtype='float')
f = np.full_like(a2,3.14)
print(f)

g = np.eye(10)
print(g,g.shape)

h = np.zeros((2,3),dtype='int32')
print(h)

a3 = np.arange(1,7,dtype='int32')
a3.shape = (2,3)
print(a3,a3.dtype)
a4 = a3.astype('float32')
print(a4,a4.dtype)


b2 = np.arange(1,10)
b2.shape = (3,3)
b2_length = len(b2)
b2_size = b2.size
print(b2_length,b2_size)


e = np.arange(1,19)
e.shape = (3,2,3)
print(e)
print(e[0][0][0])


#######################自定义复合数据类型##################
data = [('张三',16,[96,54,60]),
        ('李四',15,[65,76,89]),
        ('王五',16,[87,90,76])]
#fh = np.array(data)
#旧版本numpy会报错 ValueError: setting an array element with a sequence,
# 需要告诉它每个元素的数据类型
fh = np.array(data,dtype='U2,int32,3int32')
#U2:Unicode 字符串2个
#int32:默认
#3int32:3个int32
print(fh)
print('李四的成绩:',fh[1]['f2'])#李四的成绩 [65 76 89]
#也可以这么写
print('李四的成绩2:',fh[1][2])#李四的成绩2: [65 76 89]


fh2 = np.array(data,dtype=[
    ('name','str_',2),
    ('age','int32',1),
    ('scores','int32',3),
])
print("李四的成绩3:",fh2[1]['scores'])

fh3 = np.array(data,dtype={
    'names':['name','age','scores'],
    'formats':['U2','int32','3int32']
})
print("李四的成绩4:",fh3[1]['scores'])

#效率更高一点
fh4 = np.array(data,dtype={
    #0,28,16 从首字节开始偏移多少字节开始输出
    'name':('U3',0),#U3从0~12字节,12~16预留下来,防止可变字节
    'age':('int32',16),
    'scores':('3int32',32)
})
print("李四的成绩5:",fh4[1]['scores'])

f = np.array(['2011','2012-02-23 16:23:41','2013-12-21 13:23:01','2011-05-01'])
g = f.astype('M8[Y]')
print(g)
h = g.astype('int32')
print(h)
print(h[1] - h[0])


#############################维度####################
a = np.arange(1,9)
b = a.reshape(2,4)
d = a.flatten()
print(a.shape)
print(b.shape)
e = b.copy()
a[0] = 999
print(a,b)

c = b.ravel()
print(c)

print(d)
print(e)
a.resize(4,2)
print(a)

#############################切片####################
a = np.arange(1,10)
print(a[:-4:-1])
print(a[-4:-7:-1])
print(a[::3])
print(a[1::3])
print(a[2::3])
print("#"*10)
#############################掩码####################
a = np.arange(1,11)
mask = a % 2 == 0
print(a[mask])

b = np.arange(1,101)
mask2 = (b % 3 ==0) | (b % 7 ==0)
print(b[mask2])


#############################合并拆分####################
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
c = np.vstack((a,b))
d = np.hstack((a,b))
e = np.dstack((a,b))
#print("ab垂直组合",c)
#print("ab水平组合",d)
print("a:",a)
print("b:",b)
print("ab深度组合",e)
#print("ab垂直拆分",np.vsplit(c,2))
#print("ab水平拆分",np.hsplit(d,2))
print("ab深度拆分",np.dsplit(e,2))


a = a.ravel()
b = b.ravel()
f = np.concatenate((a,b),axis=0)
print(f)
g = np.row_stack((a,b))
print(g)
h = np.column_stack((a,b))
print(h)


############################# 其他属性 ####################
a = np.array([[1+1j,2+4j,3+7j],
                [4+2j,5+5j,6+8j],
                [7+3j,8+6j,9+9j],
              ])
print('*'*10)
print(a.size)#9
print(a.shape)#(3, 3)
print(a.dtype)#complex128
print(a.ndim)#2
print(a.itemsize)#16
print(a.nbytes)#144
print(a.real,a.imag,sep="\n")
#实部
#[[ 1.  2.  3.]
# [ 4.  5.  6.]
# [ 7.  8.  9.]]
#虚部
#[[ 1.  4.  7.]
# [ 2.  5.  8.]
# [ 3.  6.  9.]]
print(a.T)
#转置
#[[ 1.+1.j  4.+2.j  7.+3.j]
# [ 2.+4.j  5.+5.j  8.+6.j]
# [ 3.+7.j  6.+8.j  9.+9.j]]

print([i for i in a.flat])
#扁平迭代
#[(1+1j), (2+4j), (3+7j), (4+2j), (5+5j), (6+8j), (7+3j), (8+6j), (9+9j)]

print(a.tolist())
#转列表
#[[(1+1j), (2+4j), (3+7j)], [(4+2j), (5+5j), (6+8j)], [(7+3j), (8+6j), (9+9j)]]