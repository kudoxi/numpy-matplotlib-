import  matplotlib_loadtext.pyplot as plt
import numpy as np

'''
n = 1000
x = np.linspace(0,8*np.pi,n)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
plt.figure('FIll',facecolor='lightgray')
plt.title("FIll",fontsize=16)
plt.xlabel("X",fontsize=12)
plt.ylabel("Y",fontsize=12)
plt.plot(x,sinx,color='dodgerblue',label=r'$y=sin(x)$')
plt.plot(x,cosx,color='orangered',label=r'$y=\frac{cos(\frac{x}{2})}{2}$')
plt.fill_between(x,sinx,cosx,sinx > cosx,alpha=0.6,color='dodgerblue')
plt.fill_between(x,sinx,cosx,sinx < cosx,alpha=0.6,color='orangered')
plt.legend()
plt.show()
'''
#正态分布 1cigema置信区间填充颜色
x = np.linspace(60,260,1000)
cigema = 20
miu = 172
fx = 1 / (cigema * (2 * np.pi)**0.5) * np.exp(-(x - miu)**2 / (2 * cigema**2))
plt.plot(x,fx,color='dodgerblue')
fanwei = x[(x>miu) & (x<miu+cigema)]
fx2 = 1 / (cigema * (2 * np.pi)**0.5) * np.exp(-(fanwei - miu)**2 / (2 * cigema**2))
y = np.zeros(fanwei.size)
plt.fill_between(fanwei,fx2,y,fx2 > y,alpha=0.6,color='dodgerblue')
plt.show()
