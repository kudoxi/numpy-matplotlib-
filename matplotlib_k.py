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
dates = dates.astype(md.datetime.datetime)
#绘制收盘价的折线图
plt.figure('K line')
plt.xlabel("date")
plt.ylabel("rise")

rise = closing_prices <= opening_prices
#涨价　边缘色红色　填充色白色
# 跌价　边缘色绿色，填充色绿色
#填充色整理
facecolor = np.array([('white' if x else 'green') for x in rise])
#边缘色
ecolor = np.array([('red' if x else 'green')for x in rise])

#绘制影线
plt.vlines(dates,lowest_prices,highest_prices,color=ecolor)
#绘制实体
plt.bar(dates,closing_prices - opening_prices,0.8,opening_prices,facecolor=facecolor,edgecolor=ecolor,zorder=3)

plt.legend()
plt.show()
