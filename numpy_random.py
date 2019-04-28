import numpy as np

#一个人投篮命中率０．３，尝试１０次进５个的概率
getin = np.random.binomial(10,0.3,10000)
print((getin == 5).sum() / getin.size)#0.1057

#将２５个好球和５个坏球放一起，无放回的抽出５个球，求５个球都是好球的概率
getgood = np.random.hypergeometric(25,5,5,100)
print((getgood == 5).sum() / getgood.size)#0.3