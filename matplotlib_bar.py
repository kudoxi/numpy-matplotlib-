import matplotlib_loadtext.pyplot as plt
import numpy as np

apples = np.array ([34,73,82,74,92,37,48,72,37,48,92,37])
oranges = np.array([32,78,47,32,74,83,27,94,95,48,93,47])
x = np.arange(apples.size)
plt.figure("bar",facecolor="lightgray")
plt.title("bar")
plt.xlabel("month")
plt.ylabel("sales")
plt.tick_params(labelsize=16)

#主刻度设置
ax = plt.gca()
l = plt.MultipleLocator(1)
ax.xaxis.set_major_locator(l)

plt.xticks(x,['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])

#横坐标偏移0.2,防止遮盖
plt.bar(x-0.2,apples,width=0.4,color="dodgerblue",label="apple",align="center",bottom=10)#
plt.bar(x+0.2,oranges,width=0.4,color="orangered",label="orange",align="center")
plt.legend(loc="upper left")
plt.show()
