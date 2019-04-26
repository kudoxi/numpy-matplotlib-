####################### 统计每个周一的收盘价均值，每个周二收盘价均值，....每个周五收盘价的均值　##########################
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as md

#得到周几的数字
def dmy2wday(s):
    dmy = str(s,encoding='utf-8')#先把日期格式转为字符串
    time = dt.datetime.strptime(dmy,'%d-%m-%Y')#字符串转日期
    wday = time.date().weekday()#日期转周几
    return wday

wdays,closing_prices = np.loadtxt(
    'da_data/aapl.csv',unpack=True,
    delimiter=',',usecols=(1,6),
    dtype='f8, f8',#
    converters={1:dmy2wday} #第一列转换为周几
)

#得到下标
indies = np.arange(closing_prices.size)

mon_i = indies[wdays == 0]#周一下标
tue_i = indies[wdays == 1]#周二下标
wed_i = indies[wdays == 2]#周三下标
thu_i = indies[wdays == 3]#周四下标
fri_i = indies[wdays == 4]#周五下标
print(mon_i)
print(tue_i)
print(wed_i)
print(thu_i)
print(fri_i)
#由上可以看到
#最多的有７个元素，所以其他的元素需要补位
#周一只有５个元素，需要补位２个
#其他的有６个，需要补位１个



#print(closing_prices[closing_prices.keys() == mon_i])
#把缺失的补全
#为首位补０个数，末尾补２个数，补充数字的值为０
#pad_width是在各维度的各个方向上想要填补的长度,如（（1，2），（2，2）），
# 表示在第一个维度上水平方向上padding=1,垂直方向上padding=2,
# 在第二个维度上水平方向上padding=2,垂直方向上padding=2
mon_i = np.pad(mon_i,pad_width=(0,2),mode='constant',constant_values=-1)
tue_i = np.pad(tue_i,pad_width=(0,1),mode='constant',constant_values=-1)
wed_i = np.pad(wed_i,pad_width=(0,1),mode='constant',constant_values=-1)
thu_i = np.pad(thu_i,pad_width=(0,1),mode='constant',constant_values=-1)
data = np.array([mon_i,tue_i,wed_i,thu_i,fri_i])
print(data)

def func(row):
    #下标数组
    print('row1',row)
    row = row[row != -1]
    print('row2',row)
    return closing_prices[row].max(),closing_prices[row].min(),closing_prices[row].mean()

#轴向汇总
rep = np.apply_along_axis(func,1,data)
print(rep)