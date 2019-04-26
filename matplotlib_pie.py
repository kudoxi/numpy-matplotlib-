import matplotlib_loadtext.pyplot as plt
import numpy as np

plt.figure('pie chart')
plt.title('pie chart')
values = [26,17,18,20,29,23]
spaces = [0.05,0.01,0.01,0.01,0.01,0.01]
labels = ['Python','Js','C++','Java','PHP','Go']
colors = ['dodgerblue','orangered','limegreen','violet','gold','black']
plt.axis('equal') #设置等轴比例
plt.pie(
    values,spaces,#扇形之间的间距列表,
    labels, #标签列表 显示每个区块是什么意思
    colors,#扇形颜色列表
    '%.2f%%',#百分比格式
    shadow=True, #添加阴影
    startangle=0, #起始角度
)
plt.legend()
plt.show()