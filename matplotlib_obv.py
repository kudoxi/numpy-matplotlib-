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

dates,closing_prices,volumns = np.loadtxt(
    'da_data/aapl.csv',unpack=True,delimiter=',',usecols=(1,6,7),
    dtype='M8[D],f8,f8',
    converters={1:dmy2ymd} #日月年　年月日
)

dates = dates.astype(md.datetime.datetime)
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

#plt.figure("VALE and BHP")
plt.title("VALE and BHP")
plt.xlabel("date")
plt.ylabel("diff prices")
plt.grid(linestyle=":")

#绘制ＯＢＶ
diff_prices = np.diff(closing_prices)
sign_prices = np.sign(diff_prices)#转为信号量
obvs = volumns[1:] * np.abs(sign_prices)#从第二天开始算成交量
c = np.zeros_like(sign_prices).astype("str_")
c[sign_prices == -1] = 'green'
c[sign_prices >= 0] = 'red'
print(sign_prices)
plt.bar(dates[1:],obvs,0.9,color=c[1:],label="OBV",alpha=0.6)

plt.legend()
plt.show()
