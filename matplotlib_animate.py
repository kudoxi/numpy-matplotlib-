import matplotlib.animation as ma
import matplotlib.pyplot as plt
import numpy as np


'''
n = 100
balls = np.zeros(n,dtype={
    'names': ['position','size','growth','color'],
    'formats':['2f','f','f','3f']
})
#均匀分布　
balls['position'] = np.random.uniform(0,1,(n,2))#0~1 n行　２列
balls['color'] = np.random.uniform(0,1,(n,3))
balls['size'] = np.random.uniform(50,70,n)#50~70 n行
balls['growth'] = np.random.uniform(10,20,n)
plt.figure("balls animation")
plt.title("balls animation")
plt.xticks([])
plt.yticks([])
sc = plt.scatter(balls['position'][:,0],balls['position'][:,1],s=balls['size'],color=balls['color'],alpha=0.8)
#随机生成各种颜色，大小，位置的１００个气泡，并使他们不断增大
def update(number):
    balls['size'] += balls['growth']
    print(balls['size'])
    boom_i = number % 100 #100个球的下标
    balls[boom_i]['size'] = np.random.uniform(50,70,1)
    balls[boom_i]['position'] = np.random.uniform(0,1,(1,2))
    # 更新每个球的大小
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])


anim = ma.FuncAnimation(
    plt.gcf(),update,interval=30
)
plt.show()
'''
############################## 电信号 #####################3
plt.figure("signal")
plt.title("signal")
plt.xlim(0,10)
plt.ylim(-3,3)
plt.grid(linestyle=":")
pl = plt.plot([],[],color="dodgerblue",label="signal")[0]

x = 0

def update(data):
    t,v = data
    x,y = pl.get_data()
    print(x)

    x = np.append(x,t)
    y = np.append(y,v)
    pl.set_data(x,y)
    #移动坐标轴
    if(x[-1] > 10):
        plt.xlim(x[-1] - 10,x[-1])

def generator():
    global x
    y = np.sin(2 * np.pi*x) * np.exp(np.sin(0.2*np.pi*x))
    yield  (x,y)
    x += 0.05


anim = ma.FuncAnimation(
    plt.gcf(),update,generator,interval=30
)
plt.legend()
plt.tight_layout()
plt.show()