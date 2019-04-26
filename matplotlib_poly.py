import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as md

'''
x = np.linspace(-20,20,1000)
y = 4*x**3 + 3*x**2 - 1000 *x +1
P = [4,3,-1000,1]
#求导
Q = np.polyder(P)
#求根
xs = np.roots(Q)
#求函数值
ys = np.polyval(P,xs)
plt.scatter(xs,ys,marker='D',zorder=3,color="red",s=50)

plt.plot(x,y)
plt.show()
'''

######################## 使用多项式函数，拟合两支股票的差价样本数据　##############################
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

'''
diff_prices = bhp_closing_prices - vale_closing_prices
plt.plot(bhp_dates,diff_prices,color="dodgerblue",linestyle="--",label="diff prices",alpha=0.8)
plt.scatter(bhp_dates,diff_prices,c="steelblue",s=50)

#针对差价函数，执行多项式拟合
days = bhp_dates.astype("M8[D]").astype("int32")
P = np.polyfit(days,diff_prices,4)
polyline = np.polyval(P,days)
plt.plot(bhp_dates,polyline,color="orangered",linestyle="-",label="poly line")
#拐点
Q2 = np.polyder(P)
xs = np.roots(Q2)
ys = np.polyval(P,xs)
plt.scatter(xs.astype("M8[D]").astype(dt.date),ys,marker='D',zorder=3,color="red",s=50)

'''
#收益率　＝　今天的收盘价　／　昨天的收盘价
incomes = np.zeros(bhp_closing_prices.size)#第一天获取不到昨天的，从第二天开始才有收益率
for k in range(bhp_closing_prices.size):
    if k > 0:
        incomes[k,] = bhp_closing_prices[k] / bhp_closing_prices[k-1]

plt.plot(bhp_dates[1:],incomes[1:],color="red",linestyle="--",label="income rate line")
#平滑曲线
#降维
k = np.exp(np.linspace(-1,0,5))
k = k[::-1]
k /= k.sum()
s = np.convolve(incomes[1:],k,'valid')
plt.plot(bhp_dates[1:][4:],s,color="pink",linestyle="-",label="income rate-convolve line")

#拟合
dates = bhp_dates[1:][4:].astype("M8[D]").astype("int32")
P = np.polyfit(dates,s,4)
incomeline = np.polyval(P,dates)
dates2 = dates.astype("M8[D]").astype(dt.date)
plt.plot(dates2,incomeline,color="brown",linestyle="-",linewidth=2,label="income rate-fit line")


plt.legend()
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()


