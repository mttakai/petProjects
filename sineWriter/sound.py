"""
Exercises in Python
by Marjorie Takai

Created in 2017, Jan 06

create a wave sine and record as a wav file

"""


from scipy.io.wavfile import write
import numpy as np
import matplotlib as plt
import plotly.plotly as py

def createSin (freq, duration, fps=48000):
    x = np.arange(0,duration*fps)
    xr= 2*np.pi*x*freq/fps
    y = np.sin(xr)
    
    return x,y
    
def writeWave(wave, name, fps=48000):
    write(str(name)+'.wav',fps,wave)
    

def cSin(freq, length,fs = 48000):
    
    ts = 1/fs
    t = np.arange(0, length, ts)
    
    y = np.sin(2*np.pi*freq*t)
    n = float(len(y))
    
    T = n/fs
    k = np.arange(n)
    frq = float(k/T)
    frq = frq[range(n/2)]
    
    Y = np.fft.fft(y)
    Y = Y[range(n/2)]
    
    fig, ax = plt.subplots(2,1)
    ax[0].plot(t,y)
    ax[1].plot(frq,abs(Y),'r')
    plot_url= py.plot_mpl(fig,filename='fft')