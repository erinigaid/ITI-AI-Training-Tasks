import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.signal.filter_design import sos2tf

f1 = 25
f2 = 50
t = np.linspace(0 , 1 , 1000 )
sig = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)
fig, (ax1 , ax2) = plt.subplots(2 , 1 , sharex= True)
ax1.plot (t,sig)
ax1.set_title ('25 Hz and 50 Hz sinusoids')
ax1.axis ([0 , 1 , -2 , 2])
sos = signal.butter(50 , 35 , 'lp' , fs=1000 , output='sos')
filtered = signal.sosfiltfilt (sos , sig)

ax2.plot ( t , filtered)
ax2.set_title ('After 35 Hz Low-pass filter')
ax2.axis ([0,1,-2,2])
ax2.set_xlabel ('Time [seconds]')
plt.tight_layout()
plt.show()


