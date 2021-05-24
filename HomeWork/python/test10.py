#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x=np.arange(-2*np.pi,2*np.pi,0.01)
# y=np.sin(x)
# plt.subplot(221)
# plt.title("y=sin(x)")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xticks([-2*np.pi,-np.pi,0,np.pi,2*np.pi],['$-2\pi$','$-\pi$','0','$\pi$','$2\pi$'])
# plt.plot(x,y,':')

# data_0=np.load('./iris.npz',allow_pickle=True)
# value=data_0['data']
# plt.subplot(222)
# plt.scatter(value[:,0],value[:,1])

# plt.subplot(223)
# plt.hist(data_0)

data_1=np.load('./economic.npz',allow_pickle=True)
print(data_1.files)
print(data_1['columns'])
print(data_1['values'])
# plt.subplot(224)
# plt.pie(data_1)
# plt.show()
