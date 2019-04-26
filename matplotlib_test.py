import numpy as np
import matplotlib_loadtext.pyplot as plt
import random
import matplotlib_loadtext.gridspec as mg
'''
x = np.array([23,44,23,46,34,56,12,65,34])
y = np.array([65,23,76,45,31,87,67,45,96])

#核心api
plt.plot(x,y)
plt.show()

#绘制垂直线和水平线
plt.vlines(23,0,90)#垂直线
#plt.hlines(65,0,100)#一条水平线
plt.hlines([65,70],0,100)#多条水平线
plt.show()
'''

#线型,线宽,颜色
x =np.linspace(-np.pi,np.pi,1000)
y = np.sin(x)
y2 = 1/2 * np.cos(x)
plt.plot(x,y,
         linestyle='--', #线型 直线'-' 虚线'--','点线':'
         linewidth=1, #线宽 1 2 3
         color='blue', #颜色 可以写常见的英文单词/首字母  可以写#abc123  #可以写元组(0,0,0,1)/(0,0,0)这里设置过透明度就不用再设置alpha了
         alpha=0.8, #透明度
         label="sin(x)"
         )
plt.plot(x,y2,color="red",alpha=0.8,
         label=r"$\frac{cos(x)}{2}$")

#设置坐标轴范围
plt.xlim(-4,3)
plt.ylim(-3,2)

#设置刻度
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\frac{\pi}{2}$',0,r'$\frac{\pi}{2}$',r'$\pi$'])
plt.yticks([-1,-1/2,0,1/2,1])

#设置坐标轴
ax = plt.gca()
axis_t = ax.spines['top']
axis_r = ax.spines['right']
#去掉上右轴
axis_t.set_color("none")#设置为none时,去掉坐标轴
axis_r.set_color("none")
#左下轴挪到中间
axis_l = ax.spines['left']#可以拿到某个坐标轴 填入 left right top bottom
axis_b = ax.spines['bottom']
axis_l.set_position(('data',0))#元组,挪到坐标系的参照位置
axis_b.set_position(('data',0))

#绘制图例
plt.legend(loc="upper left")#best 最优 left right lower upper center正中间 lower left 左下; lower right右下...

#绘制特殊点
s_x = np.array([-np.pi/2,np.pi/2])
s_y = np.sin(s_x)
plt.scatter(s_x,s_y,
            marker="D",#点型 'D' ,'s' ,'o' ........
            s=60,    #点的大小
            color="yellow",   #颜色  edgecolor边缘色 facecolor填充色
            zorder=3 #绘制点所使用的图层编号,编号越大,图层越靠上
            )
#给点加备注
plt.annotate(
    r'$[\frac{\pi}{2},1]$',#备注文本
    xycoords='data',#当前备注目标点的信息,data表示目标点在数据坐标系上
    xy=(np.pi/2,1),       #当前备注目标点的坐标
    textcoords='offset points',#表示备注在偏移量坐标系上,和坐标点有一定的距离便宜,防止遮盖
    xytext=(30,20),   #定义备注目标点的偏移量
    fontsize=18,    #字体大小
    arrowprops = dict(
        arrowstyle='->',      #箭头样式 '-[' '-|>'
        connectionstyle='angle3', #连接线样式 bar arc
    )
)
plt.annotate(
    r'$[-\frac{\pi}{2},-1]$',
    xycoords="data",
    xy=(-np.pi/2,-1),
    textcoords="offset points",
    xytext=(10,-40),
    fontsize=18,
    arrowprops = dict(
        arrowstyle="-|>",
        connectionstyle="angle3"
    )
)
plt.show()

################################### 高级绘图 ##########################################
plt.figure('figureA',    #窗口标题
           #figsize=(100,100), #窗口大小
           facecolor='lightgray' #facecolor窗口底色
           )
plt.plot([0,1],[1,2]) #作用于figureA

plt.figure('figureB',facecolor="gray")
plt.plot([0,1,5],[1,2,3]) #作用于figureB

plt.figure('figureA')#把窗口A置为当前窗口,在之前的基础上继续绘制figureA
plt.plot([5,3,4],[5,4,5])

#图表的标题
plt.title('title',fontsize=12)
#x轴标签
plt.xlabel('number',fontsize=12)
#y轴标签
plt.ylabel('money')
#设置刻度文本的大小
plt.tick_params(labelsize=10)
#设置网格
plt.grid(linestyle=':')
#紧凑布局
plt.tight_layout()

plt.show()

#子图
#矩阵式布局 网格式布局 自由布局
#矩阵式布局
plt.figure('multi map')
for i in range(1,10):
    plt.subplot(3,3,i)#3行3列第1个
    plt.text(0.5,0.5,str(i),ha="center",va="center",size=36,alpha=0.5)#ha 水平居中 va 垂直居中
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()
plt.show()

#网格式布局
#import matplotlib.gridspec as mg
plt.figure("Grid layout")
gs = mg.GridSpec(3,3)#3行3列网格对象
plt.subplot(gs[0,:2])#第1行,前2列合并
plt.text(0.5,0.5,str(1),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[:2,2])#前2行,第3列合并
plt.text(0.5,0.5,str(2),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1,1])#第2行,第2列
plt.text(0.5,0.5,str(3),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-2:,0])#后2行,第1列合并
plt.text(0.5,0.5,str(4),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(gs[2,-2:])#第三行,后2列合并
plt.text(0.5,0.5,str(5),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])


plt.tight_layout()
plt.show()

#自由布局
plt.axes([0.1,0.2,0.5,0.3])#构建一个图表  0.1,0.2为图表左下角位置在x=0.1和y=0.2的位置 0.5,0.3是整体图表的宽高,50%和30%
plt.text(0.5,0.5,str(1),ha="center",va="center",size=36,alpha=0.5)
plt.xticks([])
plt.yticks([])
plt.show()

########################### 刻度定位器 ###################################

#绘制数轴
plt.figure('Locators',facecolor="lightgray")
locators = ['plt.NullLocator()','plt.MultipleLocator(1)','plt.MaxNLocator(nbins=4)']
for i ,locator in enumerate(locators):

    plt.subplot(len(locators),1,i+1)
    ax = plt.gca()
    r_ax = ax.spines['right']
    t_ax = ax.spines['top']
    l_ax = ax.spines['left']
    r_ax.set_color('none')
    t_ax.set_color("none")
    l_ax.set_color("none")
    b_ax = ax.spines['bottom']
    plt.xlim([0,10])
    plt.yticks([])
    #plt.ylim([-1,1])
    #x轴移到data坐标系中0的位置
    b_ax.set_position(('data',0))
    #m_loc = plt.MultipleLocator(1)
    ax.xaxis.set_major_locator(eval(locator)) #设置主刻度
    mi_loc = plt.MultipleLocator(0.1)
    ax.xaxis.set_minor_locator(mi_loc)#设置副刻度

plt.show()
########################### 刻度网格线 ###################################
y = np.array([1,10,100,1000,100,10,1])
plt.figure("Grid Line")
plt.title('Grid line')
plt.xlabel('x')
plt.ylabel('y')

ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
ax.yaxis.set_major_locator(plt.MultipleLocator(250))
ax.yaxis.set_minor_locator(plt.MultipleLocator(50))
plt.tick_params(labelsize=10)
ax.grid(
    which="major",#major,minor,both
    axis="both", #x , y ,both
    linewidth=1,
    linestyle='-',
    color="red"
)
ax.grid(
    which="minor",#major,minor,both
    axis="both", #x , y ,both
    linewidth=1,
    linestyle=':',
    color="yellow"
)
plt.plot(y,color='dodgerblue',label='Line')
plt.legend()
plt.show()

#################### 半对数坐标 ###########################
plt.figure("Semilogy")
y = np.array([1,10,100,1000,100,10,1])
plt.subplot(2,1,1)
plt.title("plot")
plt.plot(y,label='Line')
plt.legend()

plt.subplot(2,1,2)
plt.title("semilogy")
plt.semilogy(y,label='Line')#把plot改为semilogy,其他都不用变

plt.legend()
plt.show()