# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo11_balls.py  动画小球
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

# 整理数据
n = 100
balls = np.zeros(100, dtype=[
    ('position', float, 2),
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 3)])

balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(50, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 3))

# 绘制图像
mp.figure('Balls Animation', facecolor='lightgray')
mp.title('Balls Animation', fontsize=14)
mp.xticks([])
mp.yticks([])
sc = mp.scatter(balls['position'][:, 0],
                balls['position'][:, 1],
                s=balls['size'],
                color=balls['color'],
                alpha=0.8)


def update(number):
    balls['size'] += balls['growth']
    boom_i = number % 100
    balls[boom_i]['size'] = np.random.uniform(50, 70, 1)
    balls[boom_i]['position'] = np.random.uniform(0, 1, (1, 2))
    # 更新每个球的大小
    sc.set_sizes(balls['size'])
    sc.set_offsets(balls['position'])

anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()
