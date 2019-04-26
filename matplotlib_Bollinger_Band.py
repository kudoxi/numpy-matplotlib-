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

dates,opening_prices,highest_prices,lowest_prices,closing_prices, volumns = np.loadtxt(
    'da_data/aapl.csv',unpack=True,
    delimiter=',',usecols=(1,3,4,5,6,7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    converters={1:dmy2ymd} #日月年　年月日
)

plt.figure("Bollinger_band")
plt.title("Bollinger")
plt.xlabel("date")
plt.ylabel("rise")

#绘制收盘价的均线
m = np.mean(closing_prices)
dates = dates.astype(md.datetime.datetime)
plt.hlines(m,dates[0],dates[-1],color='orangered',label="AVG()")#从头画到尾
plt.plot(dates, closing_prices, c='dodgerblue',
        linewidth=2, linestyle='--',
        label='Closing Prices',alpha=0.8)

#加权卷积５日均线
dates5 = dates[4:]
kernel3 = np.exp(np.linspace(-1,0,5))
kernel3 = kernel3[::-1]
kernel3 /= kernel3.sum()
sma54 = np.convolve(closing_prices,kernel3,'valid')
plt.plot(dates5,sma54,c="pink",label="SMA-54",linewidth=3)

#布林带上轨和下轨
stds = np.zeros(closing_prices.size-4)
for i in range(stds.size):
    stds[i] = np.std(closing_prices[i:i+5])

uppers = sma54 + 2 * stds
lowers = sma54 - 2 * stds

plt.plot(dates5,uppers,c="steelblue",label="uppers")
plt.plot(dates5,lowers,c="steelblue",label="lowers")
plt.fill_between(dates5,uppers,lowers,uppers > lowers,color="dodgerblue",alpha=0.3)

plt.legend()
plt.show()
