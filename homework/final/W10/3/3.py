#http://web.ntnu.edu.tw/~tsungwu/Python_DevOps/Part1_Basics&Math/section6_ODE.html
from sympy import*
from sympy.abc import V,C,R,t

V=Function('V')
ans = dsolve(Eq(Derivative(V(t), t)*C + V(t)/R, 0),V(t))
print('dsolve(Eq(Derivative(V(t), t)*C + V(t)/R, 0),V(t) =',ans)
