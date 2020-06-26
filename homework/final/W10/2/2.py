#https://medium.com/pyladies-taiwan/%E7%B2%BE%E7%A2%BA%E7%9A%84%E6%B5%AE%E9%BB%9E%E6%95%B8%E9%81%8B%E7%AE%97-28d34e652e51
from math import *

step = 0.05
def df(f, x, h=step):
    return (f(x+h)-f(x-h))/(2*h)

def dfn(f, x, n, h=step):
    if (n == 0): return f(x)
    if (n == 1): return df(f,x,h)
    return (dfn(f, x+h, n-1) - dfn(f, x-h, n-1))/(2*h)

#print('df(sin, pi/4)=', df(sin, pi/4))

for i in range(10):
    print('dfn(sin,', i, 'pi/4)=', dfn(sin, pi/4, i))
    
