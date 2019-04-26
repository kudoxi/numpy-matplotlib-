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
#print(wdays)#0是周1,1是周２.....

#把算出的均值，存入数组
avg_prices = np.zeros(5)
for wday in range(avg_prices.size):
    #print(closing_prices[wdays == wday])
    m = closing_prices[wdays == wday].mean()#分别得到closing_prices里，星期数为０，１，２，３．．．的收盘平均值
    avg_prices[wday] = m#根据星期数，放入数组


print(avg_prices)#分别为周一，周二，周三，周四，周五的收盘价均值

#联合遍历
for wday,avg_price in zip(['Mon','Tue','Wed','Thu','Fri'],avg_prices):
    print(wday,',',avg_price)

plt.plot(wdays,closing_prices,)