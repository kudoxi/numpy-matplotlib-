import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as plt
'''
A = np.random.uniform(10,30,(4,4))
A = np.floor(A)
eigvals,eigvecs = np.linalg.eig(A)
# print(eigvals,type(eigvals))
# print(eigvecs,type(eigvecs))

#逆向推导原方阵
B = np.mat(eigvecs) * np.mat(np.diag(eigvals))*np.mat(eigvecs)
print(A)
print(B.real)
#如果去掉两个特征
eigvals[2:] = 0 #抹掉后面两个特征值
C = np.mat(eigvecs) * np.mat(np.diag(eigvals))*np.mat(eigvecs)
print(C.real)

'''
###################################　图片特征提取　############################################
#一定要方阵图片
image = sm.imread('da_data/lily.jpg',True)#True　灰度处理
#print(image.shape)
#对image提取特征值和特征向量
eigvals,eigvecs = np.linalg.eig(image)
#eigvals[200:] = 0
image2 = np.mat(eigvecs) * np.mat(np.diag(eigvals))*np.mat(eigvecs)
print("image:",image)
print("image2:",image2)

plt.figure("Img eig")
plt.subplot(1,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(image,cmap='gray')#设置为从黑到白的映射

plt.subplot(1,2,2)
plt.xticks([])
plt.yticks([])
plt.imshow(image2.real,cmap='gray')#设置为从黑到白的映射

plt.tight_layout()
plt.show()
