# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
dem10_anim.py  简单动画
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma


def update(number):
    print(number)

mp.figure('Animation')
anim = ma.FuncAnimation(
    mp.gcf(), update, interval=1000)
mp.show()
