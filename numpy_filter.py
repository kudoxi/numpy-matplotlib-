import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf
import numpy.fft as nf

sample_rates ,noised_sigs = wf.read('da_data/noised.wav')
print('sample_rates:',sample_rates)
print('noised_sigs:',noised_sigs.shape)
# sample_rates: 44100
# noised_sigs: (220500,)
#绘制音频的时域图像
times = np.arange(len(noised_sigs)/sample_rates,len(noised_sigs)+5)#x轴　0 1/44100 2/44100 3/44100 ... 220500/44100

plt.figure('filter')

plt.subplot(221)
plt.title('time domain')
plt.ylabel('signal')
plt.grid(linestyle=':')
plt.plot(times[:200],noised_sigs[:200],color='dodgerblue',label='nosed sign')
plt.legend()

#基于傅里叶变换，获取音频频域信息，绘制音频频域的　频域／能量图像
complex_noised = nf.fft(noised_sigs)#含有噪音的复数信号数组
pows = np.abs(complex_noised)#取模
freqs = nf.fftfreq(times.size,1/sample_rates)
plt.subplot(222)
plt.title('frequency domain')
plt.ylabel('signal')
plt.grid(linestyle=':')
plt.semilogy(freqs[freqs>0],pows[freqs>0],color='orangered',label='nosed sign')


#可以看到，底部有很多低频，属于噪声，应该去除
#找到能量最高的下标，只保留它一个能量，其他的复数全部改为０
fund_freqs = freqs[pows.argmax()]#得到频率最高的频率
noised_indices = np.where(freqs != fund_freqs)#获取所有噪声频率的下标数组
complex_filter = complex_noised.copy()
complex_filter[noised_indices] = 0 #过滤噪声
filter_pows = np.abs(complex_filter)#取模
print(filter_pows.shape)

#将低频噪声去除，绘制音频频域的：频率／能量图像
plt.subplot(223)
plt.title('filter domain')
plt.ylabel('powers')
plt.grid(linestyle=':')
plt.plot(freqs[freqs>0],filter_pows[freqs>0],color='orangered',label='nosed sign')


#逆向傅里叶变换，生成新的音频信号，绘制音频时域图：时间／位移图像
filter_sigs = nf.ifft(filter_pows)
plt.subplot(224)
plt.title('filtered time domain')
plt.ylabel('signal')
plt.grid(linestyle=':')
plt.plot(times[:200],filter_sigs[:200].real,color='orangered',label='nosed sign')

plt.tight_layout()
plt.legend()
plt.show()

#生成音频文件
wf.write('new_noise.wav',sample_rates,filter_sigs.real.astype(np.int16))#filter_sigs.real,16位int
