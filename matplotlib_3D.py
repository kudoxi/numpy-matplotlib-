import matplotlib_loadtext.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
'''
########################### 散点图　################################
plt.figure("3D")
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
plt.tick_params(labelsize=10)
x = np.random.normal(100,10,500)
y = np.random.normal(200,20,500)
z = np.random.normal(300,30,500)
d = (x-100)**2 + (y - 200) **2 + (z - 300)**2
#调用axes3d的方法绘制3D散点图形
ax3d.scatter(x,y,z,marker='o',s=60,c=d,cmap='jet_r',zorder=3)#,edgecolor='',facecolor=''
plt.show()


########################### 线框图　################################
plt.figure("wireframe")
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
n  = 1000
#公式需要,x y 从-3 到 3取n个点
x ,y = np.meshgrid(np.linspace(-3,3,n),
            np.linspace(-3,3,n))#构建网格点坐标矩阵
#通过数学公式,计算每个网格点的高度
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y **2)

ax3d.plot_wireframe(x,y,#网格点坐标矩阵
                    z,#每个坐标的高度值
                    rstride=30,#row stride 行跨距
                    cstride=30,#column stride 列跨距
                    linewidth=1,color='dodgerblue')

plt.show()
'''

########################### 曲面图　################################
plt.figure("wireframe")
ax3d = plt.gca(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
n  = 1000
#公式需要,x y 从-3 到 3取n个点
x ,y = np.meshgrid(np.linspace(-3,3,n),
            np.linspace(-3,3,n))#构建网格点坐标矩阵
#通过数学公式,计算每个网格点的高度
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y **2)
ax3d.plot_surface(x,y,#网格点坐标矩阵
                    z,#每个坐标的高度值
                    rstride=30,#row stride 行跨距
                    cstride=30,#column stride 列跨距
                    cmap='jet')#color='dodgerblue'linewidth=1,
plt.tight_layout()
plt.show()