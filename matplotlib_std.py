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
# 求出closing_prices的标准差
std1 = np.std(closing_prices)
std2 = np.std(closing_prices, ddof=1)
print(std1, std2)

# 手动计算
m = closing_prices.mean()  # 均值
D = closing_prices - m   # 离差数组
Q = D**2  # 离差方数组
v = Q.sum() / Q.size  # 总体方差
s = np.sqrt(v)  # 总体标准差
print(s)
v = Q.sum() / (Q.size - 1)  # 样本方差
s = np.sqrt(v)  # 样本标准差
print(s)