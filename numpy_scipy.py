import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt
import scipy.integrate as sia
import scipy.misc as sm
import scipy.ndimage as sn
'''
#####################################　插值器　#############################################
#构建原始的散点数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x,max_x,13)
dis_y = np.sinc(dis_x)

plt.scatter(dis_x,dis_y,c="red",s=60,label='origin')

#以这些散点为参数，获取插值器函数
linear = si.interp1d(dis_x,dis_y,kind='linear')
cubic = si.interp1d(dis_x,dis_y,kind='cubic')#三次样条插值器

dis_x2 = np.linspace(min_x,max_x,1000)
dis_y2 = linear(dis_x2)
dis_y3 = cubic(dis_x2)

plt.plot(dis_x2,dis_y2,c="dodgerblue",label='linear')
plt.plot(dis_x2,dis_y3,c="orangered",label='cubic',alpha=0.5,linewidth=2)


plt.legend()
plt.show()

'''
'''
#####################################　积分　#############################################
#直观地说，对于一个给定的正实值函数，在一个实数区间上的定积分，可以理解为：
#坐标平面上由曲线，直线，轴组成的曲边梯形的面积值（一个确定的实数值）

#案例，y=2x**2 + 3x + 4在［－５，５］区间的函数图像的定积分的值
def f(x):
    return 2*x**2 + 3*x + 4

a,b = -5,5
x = np.linspace(a,b,1000)
y = f(x)
#利用微元法求积分
n = 50
x2 = np.linspace(a,b,n+1)
y2 = f(x2)
area = 0
for i in range(n):
    area += (y2[i]+y2[i+1]) * (x2[i+1] - x2[i]) * 0.5

print("微元法：",area)#206.8

#用scipy求积分
area = sia.quad(f,a,b)[0]
print("scipy：",area)#206.66666666666669

plt.figure('intergral')
plt.title("intergral")
plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle=":")

ax = plt.gca()
l = plt.MultipleLocator(1)
ax.xaxis.set_major_locator(l)

plt.plot(x,y,color="dodgerblue",linewidth=5,alpha=0.5,label='f(x)')
plt.fill_between(x,f(x),0,f(x)>0,alpha=0.5,color='dodgerblue')
plt.legend()
plt.show()
'''
#####################################　图像处理　#############################################

image = sm.imread('da_data/lily.jpg',True)
#高斯模糊
image2 = sn.median_filter(image,21)
#角度旋转　
image3 = sn.rotate(image,45)
# 边缘识别
image4 = sn.prewitt(image)

plt.figure('image')
plt.xticks([])
plt.yticks([])
plt.subplot(221)
plt.imshow(image,cmap='gray')

plt.xticks([])
plt.yticks([])
plt.subplot(222)
plt.imshow(image2,cmap='gray')

plt.xticks([])
plt.yticks([])
plt.subplot(223)
plt.imshow(image3,cmap='gray')

plt.xticks([])
plt.yticks([])
plt.subplot(224)
plt.imshow(image4,cmap='gray')
plt.show()
