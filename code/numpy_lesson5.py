import numpy as np
a = np.arange(1, 7).reshape(2, 3)
print("a =\n", a)
b = a                    
b[0, 0] = 999
print("\n改 b 之后，a =\n", a)  
c=a.view()
c[0,0]=666
print("\n改c之后,a=\n",a)
d=a.copy()
d[0,0]=333
print("改d之后，a=\n",a)
print("\n是不是同一个东西：")
print("a is b ?", a is b)
print("a is c ?", a is c)
print("a is d ?", a is d)