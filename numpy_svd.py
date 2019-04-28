import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as plt

M = np.mat('23 24 55;22 65 23')
U,S,V = np.linalg.svd(M,full_matrices=False)#Ｔrue时表示想要完整矩阵
print(U,U.shape)
print(S,S.shape)
print(V,V.shape)
print(U * U.T)
print(V * V.T)
print(U * np.mat(np.diag(S)) * V)


image = sm.imread('da_data/lily.jpg',True)#True　灰度处理
u,sv,v = np.linalg.svd(image)
eigvals,eigvecs = np.linalg.eig(image)
eigvals[50:] = 0
image2 = np.mat(eigvecs) * np.mat(np.diag(eigvals))*np.mat(eigvecs).I
sv[50:] = 0
image3 = u * np.mat(np.diag(sv)) * v
plt.figure("Img eig")
plt.subplot(2,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(image,cmap='gray')#设置为从黑到白的映射

plt.subplot(2,2,2)
plt.xticks([])
plt.yticks([])
plt.imshow(image2.real,cmap='gray')#设置为从黑到白的映射

plt.subplot(2,2,3)
plt.xticks([])
plt.yticks([])
plt.imshow(image3.real,cmap='gray')#设置为从黑到白的映射

plt.tight_layout()
plt.show()