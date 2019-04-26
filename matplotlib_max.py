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
dates = dates.astype(md.datetime.datetime)

plt.plot(dates, closing_prices, c='dodgerblue',
        linewidth=2, linestyle='--',
        label='Closing Prices')
# 评估AAPL股价波动性
max_v = np.max(highest_prices)
min_v = np.min(lowest_prices)
print(min_v, '~', max_v)

# 查看AAPL最大、小值的日期，分析为什么会出现这种情况
max_i = np.argmax(highest_prices)
min_i = np.argmin(lowest_prices)
print('max date:', dates[max_i])
print('min date:', dates[min_i])


#对比两个数组大小
a = np.arange(1, 10).reshape(3, 3)
b = a.ravel()[::-1].reshape(3, 3)
print(a, b, sep='\n')
print(np.maximum(a, b))
print(np.minimum(a, b))

#中位数
closing_prices = np.msort(closing_prices)#数组由小到大
median = np.median(closing_prices)#得到中位数
plt.hlines(median, dates[0], dates[-1],
          color='green', label='Median')

plt.legend()
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()