import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as md

#把字符串日月年转为年月日字符串
def dmy2ymd(s):
    dmy = str(s,encoding='utf-8')#先把日期格式转为字符串
    time = dt.datetime.strptime(dmy,'%d-%m-%Y')#字符串转日期
    ymd = time.date().strftime('%Y-%m-%d')#再转为固定格式的字符串
    return ymd

dates,opening_prices,highest_prices,lowest_prices,closing_prices = np.loadtxt(
    'da_data/aapl.csv',unpack=True,delimiter=',',usecols=(1,3,4,5,6),
    dtype='M8[D],f8,f8,f8,f8',
    converters={1:dmy2ymd} #日月年　年月日
)

#绘制收盘价的折线图
plt.figure('closing price')
plt.xlabel("date")
plt.ylabel("closing prices")
#设置刻度定位器
ax = plt.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO) #每周一为主刻度
)
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y') #设置主刻度的日期格式
)
#设置次刻度定位器为日
ax.xaxis.set_minor_locator(
    md.DayLocator()
)
#需要把dates转为matplotlib识别的datetime类型
dates = dates.astype(md.datetime.datetime)

plt.grid(linestyle=":")
plt.plot(dates,closing_prices,c="dodgerblue",linewidth=3,linestyle="--",label="closing prices")
plt.plot(dates,opening_prices,c="orangered",linewidth=3,linestyle="--",label="opening prices")
plt.legend()
plt.gcf().autofmt_xdate()#格式化日期在x轴的显示方式
plt.show()