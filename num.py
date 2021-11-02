'''import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)

import sys
import time
b=range(1000)
print(sys.getsizeof(5)*len(b))
c=np.arange(1000)
print(c.size*c.itemsize)

size=10000
l1=range(size)
l2=range(size)
a1=np.arange(size)
a2=np.arange(size)
start=time.time()
result=a1+a2
print("numpy array took",(time.time()-start)*1000)

a=np.array([[1,2],[4,3],[5,6]])
print(a)
print(a.ndim)
print(a.itemsize)
print(a.shape)
a=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
print(a)
print(a.itemsize)
b=np.array([[1,2],[3,4],[5,6]],dtype=np.complex64)
print(b.itemsize)

a=np.arange(9)
print(a)
b=a.reshape(3,3)
print("the modified array:",b)
print(b.flatten())
print(b.flatten("f"))

import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
a=np.array([20,87,4,40,53,74,56,51,11,20,40,15])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title("histogram")
plt.show()'''

import pandas as pd
import numpy as np
s=pd.Series([1,2,3,4,5,6,np.nan,8,9,10])
print(s)

d=pd.date_range('20200301',periods=10)
print(d)

df=pd.DataFrame(np.random.randn(10,4),index=d,columns=["a","b","c","d"])
print(df)

a=pd.DataFrame({'a':[1,2,3,4],
                'b':pd.Timestamp('20200301'),
                'c':pd.Series(1,index=list(range(4)),dtype='float32'),
                'd':np.array([5]*4,dtype='int32'),
                'e':pd.Categorical(['true','False','True','False']),
                'f':'sonata'})
print(a)
print(a.dtypes)
print(a.head())
print(a.tail())
print(a.index)
print(a.columns)