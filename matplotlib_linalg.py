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

#绘制收盘价的均线
m = np.mean(closing_prices)
dates = dates.astype(md.datetime.datetime)
plt.hlines(m,dates[0],dates[-1],color='orangered',label="AVG()")#从头画到尾
plt.plot(dates, closing_prices, c='dodgerblue',
        linewidth=2, linestyle='--',
        label='Closing Prices',alpha=0.8)


#绘制股价预测线，假设股价符合N元线性关系
#用前６个数据，３个未知数变量，预测第７个
N = 3
#pred_prices 存储每个股价预测值
pred_prices = np.zeros(closing_prices.size - 2*N + 1)#解出３个３元１次方程，需要消耗５个数，这５个数不在预测范围内
for i in range(pred_prices.size):
    A = np.zeros((N, N))
    for j in range(N):
        A[j,] = closing_prices[j+i:j+i+N]#i=0时，j~j+N作为Ａ，i=1时，往后挪一位，j+1~j+N作为Ａ，依次下去

    B = closing_prices[N+i:i+N*2]#3,4,5　Ｂ同理
    r = np.linalg.lstsq(A,B)[0]
    pred_price = B.dot(r)#B和r做点乘
    pred_prices[i] = pred_price

#这里不能用pandas判断日期是否为周六日，去掉pred_prices最后一个数据，保证维度相同
pred_prices = pred_prices[:-1]
plt.plot(dates[2*N:], pred_prices,'o-', c='orangered',
        linewidth=2, linestyle='--',
        label='pred prices',alpha=0.8)

#线性拟合
#（最高价＋最低价＋收盘价）／３用这３０个点去找拟合线
trend_points = (highest_prices + lowest_prices+closing_prices )/3#趋势点价格
plt.scatter(dates,trend_points,s=60,color="pink",label="trend points")
#整理矩阵　日期转为数字，参与计算
days = dates.astype('M8[D]').astype("int32")
A = np.column_stack((days,np.ones_like(days)))#列合并 第一列日期的数字类型，第二列１
B = trend_points
r = np.linalg.lstsq(A,B)[0]
k = r[0]
b = r[1]

plt.plot(dates,k*days + b,color="green",label="trend_line")
#绘制顶部压力线　趋势线　＋　（最高－最低）
cha_prices = highest_prices - lowest_prices
#压力趋势线
r2 = np.linalg.lstsq(A,k*days + b + cha_prices)[0]
#支撑趋势线
r3 = np.linalg.lstsq(A,k*days + b - cha_prices)[0]
plt.plot(dates,r2[0] * days + r2[1],color="green",label="press trend line",marker="+")
plt.plot(dates,r3[0] * days + r3[1],color="green",label="support  line",marker="+")
#压力线
plt.plot(dates,k*days + b + cha_prices,color="green",label="press line",marker="p")
#支撑线
plt.plot(dates,k*days + b - cha_prices,color="green",label="support line",marker="p")


plt.legend(loc='lower left')
plt.show()