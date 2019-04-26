import numpy as np
import matplotlib_loadtext.pyplot as plt

#体重预测身高
'''
#x = weight y=height
x_y = [20,100,80,90,110,120,130,190,40,50,60,63,87] #斤
y_y = [80,170,160,165,167,172,175,176,140,143,154,156,159] #cm
plt.scatter(x_y,y_y,color="yellow",alpha=0.9,s=60)

x_b = [26,120,87,94,122,136,147,206,47,57,63,67,95]
y_b = [92,184,173,174,192,189,192,184,153,159,169,169,173] #cm
plt.scatter(x_b,y_b,color="black",alpha=0.5,s=60)

x_w = [34,98,92,98,114,128,138,197,48,58,63,69,92] #斤
y_w = [89,179,166,168,175,183,187,189,164,156,168,163,169] #cm
plt.scatter(x_w,y_w,color="gray",alpha=0.5,s=60)

plt.show()
'''
#生成符合正态分布的随机数据
n = 500
x = np.random.normal(172,20,n)#172是期望,20标准差,500个数
y = np.random.normal(60,10,n)
plt.figure('Persons',facecolor='lightgray')
plt.title("Persons",fontsize=16)
plt.xlabel("weight",fontsize=12)
plt.ylabel("height",fontsize=12)
plt.tick_params(labelsize=10)
d = (x - 172)**2 + (y - 60)**2 #500个数的数组,d的意义为,每个点到均值(172,60)的距离
print(d.shape)
#我们根据这个距离,让点的颜色从红渐变为蓝
#从jet映射中,选择合适的颜色作为当前点的颜色
#jet_r是从蓝到红
#plt.scatter(x,y,s=50,marker='o',color="dodgerblue",label="Person points",alpha=0.8)
#color必须写成c
plt.scatter(x,y,s=50,marker='o',c=d,cmap='jet',label="Person points",alpha=0.8)
plt.show()