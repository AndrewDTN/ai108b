import cmath

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = cmath.sqrt(t)
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]


print("root of 2x^2+2x+2=", root2(2,2,2))
