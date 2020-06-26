#https://blog.csdn.net/haodawei123/article/details/90517274
import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4, suppress=True)
freq = random.randint(0,10)
t = np.arange(-10*np.pi, 10*np.pi, 0.1*np.pi)
# ft = 10*np.sin(t)
ft = 10*np.cos(freq*t)
fi = np.fft.ifft(ft)
fr = np.fft.fft(fi)

print('ft=', ft)
print('fr=', fr)
print('fi=', fi)


print('freq=', freq)

plt.plot(t,ft,label="$y = 10 sin(f x)$", color="red", linewidth=2)
plt.plot(t,fi,label="ifft: y$", color="blue", linewidth=2)
plt.plot(t,fr,label="fr: y$", color="white", linewidth=1)
plt.show()
