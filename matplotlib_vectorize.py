import numpy as np
import math as m
import datetime as dt
import matplotlib.dates as md
import matplotlib.pyplot as plt

'''
#函数矢量化
def foo(a,b):
    return m.sqrt(a**2+b**2)

#普通调用
print(foo(3,4))

a = np.arange(3,10)
b = np.arange(4,11)
#矢量化
print(np.vectorize(foo)(a,b))
#也可以矢量化
print(np.frompyfunc(foo,2,1)(a,b))
#frompyfunc(函数名，接收参数个数，返回值个数）
'''
#定义一种买入卖出策略，通过历史数据验证这种策略是否值得实施
#每天开盘价
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

# 设置刻度定位器
ax = plt.gca()
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO)  # 每周一为主刻度
)
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y')  # 设置主刻度的日期格式
)
# 设置次刻度定位器为日
ax.xaxis.set_minor_locator(
    md.DayLocator()
)

# plt.figure("profits")
plt.title("profits")
plt.xlabel("date")
plt.ylabel("profits")
plt.grid(linestyle=":")


#计算该策略的收益率
def profit(opening_price,highest_price,lowest_price,closing_price,rate):
    #buying_price = opening_price * 0.99 #如果比开盘价低９９％，就买,结果表明亏了

    buying_price = opening_price * rate
    if lowest_price <= buying_price <= highest_price:
        return (closing_price-buying_price) * 100 / buying_price #100是买了１００股

    return np.nan#返回无效数字
#矢量化
profits_func = np.vectorize(profit)
rates = np.linspace(0,1,100)
max_profit = 0
max_rate = 0
for rate in rates:
    profits = profits_func(opening_prices,highest_prices,lowest_prices,closing_prices,rate)
    #拿到无效值的掩码
    nan = np.isnan(profits)
    #按位取反
    profits = profits[~nan]
    dates2 = dates[~nan]
    if len(profits) > 0:

        avg = profits.mean()
        if max_profit < avg:
            max_profit = avg
            max_rate = rate

        plt.hlines(avg,dates[0],dates[-1],color='orangered',label="avg_{}".format(rate))
        plt.plot(dates2,profits,c='dodgerblue',label="profits")
plt.legend()
plt.show()
print("最大收益率：",max_profit,"最大购买比率：",max_rate)