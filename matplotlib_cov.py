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

bhp_dates,bhp_closing_prices = np.loadtxt(
    'da_data/bhp.csv',unpack=True,delimiter=',',usecols=(1,6),
    dtype='M8[D],f8',
    converters={1:dmy2ymd} #日月年　年月日
)

vale_closing_prices = np.loadtxt(
    'da_data/vale.csv',unpack=True,delimiter=',',usecols=(6,),
)
bhp_dates = bhp_dates.astype(md.datetime.datetime)

#绘制收盘价的折线图
plt.figure('COV')
plt.xlabel("date")
plt.ylabel("price")
plt.grid(linestyle=":")
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



plt.plot(bhp_dates, bhp_closing_prices, c='dodgerblue',
        linewidth=2, linestyle='--',
        label='Closing Prices',alpha=0.8)

plt.plot(bhp_dates, vale_closing_prices, c='orangered',
        linewidth=2, linestyle='--',
        label='Closing Prices',alpha=0.8)

#计算协方差
bhp_mean = bhp_closing_prices.mean()
vale_mean = vale_closing_prices.mean()
d_bhp = bhp_closing_prices - bhp_mean
d_vale = vale_closing_prices - vale_mean

cov_ab = (d_bhp * d_vale).mean()
print("协方差：",cov_ab)

#协方差矩阵
n = np.cov(bhp_closing_prices,vale_closing_prices)
print("协方差矩阵：",n)

#计算相关系数
cov_n = cov_ab / (np.std(bhp_closing_prices) *np.std(vale_closing_prices))
print("相关系数：",cov_n)

#相关矩阵
m = np.corrcoef(bhp_closing_prices,vale_closing_prices)
print("相关矩阵：",m)



plt.legend(loc='lower left')
plt.show()