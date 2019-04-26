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

#绘制收盘价的折线图
plt.figure('K line')
plt.xlabel("date")
plt.ylabel("rise")


#绘制收盘价的均线
m = np.mean(closing_prices)
dates = dates.astype(md.datetime.datetime)
plt.hlines(m,dates[0],dates[-1],color='orangered',label="AVG()")#从头画到尾
plt.plot(dates, closing_prices, c='dodgerblue',
        linewidth=2, linestyle='--',
        label='Closing Prices',alpha=0.8)


# 求出交易量加权均线 VWAP
vwap = np.average(closing_prices, weights=volumns)
plt.hlines(vwap, dates[0], dates[-1],
          color='steelblue', label='VWAP')

#时间加权平均价格
tw = np.arange(1, 31)
twap = np.average(closing_prices, weights=tw)
plt.hlines(twap, dates[0], dates[-1],
          color='violet', label='TWAP')

#5日移动均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
    sma5[i] = closing_prices[i:i+5].mean()
dates5 = dates[4:]
plt.plot(dates5,sma5,c="red",label="SMA-5",linewidth=5,alpha=0.4)

#当前几次的数据会影响当前数据时，可以使用卷积运算
#1,2,3,4,5,6,7,8,9,10,11．．．
#1/5,1/5,1/5,1/5,1/5
#numpy提供了卷积运算相关api
#array 原数组
#kernel　卷积核数组
#valid　有效卷积运算结果
#r = np.convolve(array,kernel,'valid')
kernel = np.ones(5) / 5
sma52 = np.convolve(closing_prices,kernel,'valid')
plt.plot(dates5,sma52,c="yellow",label="SMA-52")

#10日均线
kernel2 = np.ones(10)/10
sma53 = np.convolve(closing_prices,kernel2,'valid')
plt.plot(dates[9:],sma53,c="green",label="SMA-10")

#加权卷积５日均线
#卷积核一样，说明每个值的重要程度都是一样的
#卷积运算过程中，每一个价格都应对应一个权重，时间越靠后的价格求均值时的权值应越高，因为最近的数据可参考性更大
#这时候需要５个递增的核数组元素，而又不是变化太大的
#取 y = e^x ，域为[-1,0]
kernel3 = np.exp(np.linspace(-1,0,5))
kernel3 = kernel3[::-1]#核数组需要逆序，如［８，７，６］在计算时顺序是６，７，８对准原是数组
print(kernel3)
#卷积核的数比原值要大，会导致卷积计算后的值更大
#需要归一化,让每个元素和kernel3原来的元素值比例相同，但相加为１
#如kernel3为［１，２，３，４，５］时，归一化为［１／１５，２／１５，３／１５，４／１５，５／１５］
kernel3 /= kernel3.sum()

sma54 = np.convolve(closing_prices,kernel3,'valid')
plt.plot(dates5,sma54,c="pink",label="SMA-54",linewidth=3)
#由图可见，加权卷积的线比均线要左移，能更早反应规律



plt.legend()
plt.gcf().autofmt_xdate()#格式化日期在x轴的显示方式
plt.show()
