import numpy as np
import matplotlib.pyplot as mp
import numpy.fft as nf

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y1 = 4 * np.pi * np.sin(x)
y2 = 4 / 3 * np.pi * np.sin(3 * x)
y3 = 4 / 5 * np.pi * np.sin(5 * x)
y4 = 4 / 7 * np.pi * np.sin(7 * x)
n = 1000
y = np.zeros(n)
for i in range(1, n + 1):
    y += 4 / (2 * i - 1) * np.pi * np.sin((2 * i - 1) * x)

mp.figure('Signal')
mp.subplot(121)
mp.title('Time Zone', fontsize=14)
mp.plot(x, y1, label='y1', alpha=0.3)
mp.plot(x, y2, label='y2', alpha=0.3)
mp.plot(x, y3, label='y3', alpha=0.3)
mp.plot(x, y4, label='y4', alpha=0.3)
mp.plot(x, y, label='y')

# 基于傅里叶变换，拆解y
complex_ary = nf.fft(y)

y2 = nf.ifft(complex_ary)
mp.plot(x, y2.real, linewidth=7, c='red',alpha=0.4, label='y2')#可以看到合并后又完整了

mp.subplot(122)
# 采样频率=1000  采样周期为相邻两点间距离
freqs = nf.fftfreq(x.size, x[1] - x[0])
print(freqs)
pows = np.abs(complex_ary)
mp.title('Frequency Zone',  fontsize=14)
mp.plot(freqs[freqs > 0], pows[freqs > 0],color='orangered')


mp.tight_layout()
mp.legend()
mp.show()