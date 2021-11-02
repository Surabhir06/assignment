#exercise questions
#Q1
import numpy as np
bool_arr=np.ones((4,4),dtype=bool)
print(bool_arr)

#Q2
import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
a[a%2==1]=-1
print(a)

#Q3
import numpy as np
a=np.array([[11,2,3],[5,6,8],[7,65,43]])
x=np.max(a)
y=np.min(a)
print("maximum number in the matrix is:",x)
print("minimum number in the matrix is:",y)

#Q4
import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
h=np.intersect1d(a,b)
print(h)

#Q5
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
intersect=a[np.in1d(a,b)]
mask1=np.searchsorted(a,intersect)
mask2=np.searchsorted(b,intersect)
x=np.delete(a,mask1)
y=np.delete(b,mask2)
print(x)
print(y)