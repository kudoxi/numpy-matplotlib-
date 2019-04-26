import matplotlib_loadtext.pyplot as plt
import numpy as np

n  = 1000
#公式需要,x y 从-3 到 3取n个点
x ,y = np.meshgrid(np.linspace(-3,3,n),
            np.linspace(-3,3,n))#构建网格点坐标矩阵

#通过数学公式,计算每个网格点的高度
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y **2)
z = np.eye(1000)
plt.figure("imshow")
plt.title("imshow")
plt.xlabel("x")
plt.ylabel("y")
plt.tick_params(labelsize=10)
plt.grid(linestyle=":")
plt.imshow(z,cmap='jet',origin='lower')
plt.colorbar()
plt.show()