import numpy as np
A=np.arange(12).reshape((3,4))
print("原数组:",A)
print("纵向三等分:",np.split(A,3,axis=0))
print("横向四等分:",np.split(A,4,axis=1))
print("按位置分:",np.split(A,[1,2],axis=0))
print("vsplit 纵向:",np.vsplit(A,3))
print("hsplit 横向:",np.hsplit(A,4))
a=np.arange(5)
print("a:",a)
b=a
c=np.copy(a)
a[0]=99
print(b)
print(c)