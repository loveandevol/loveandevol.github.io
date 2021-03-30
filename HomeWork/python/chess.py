import numpy as np
import os
print("--------0-1 array---------->>>")
print(np.arange(0,1,0.01))
print("--------GS random---------->>>")
print(np.random.randn(10,10))
print("--------nchess------------->>>")
arr=np.zeros((8,8))
arr[0:8:2,1:8:2]=1
arr[1:8:2,0:8:2]=1
for i in range(8):
    for j in range(8):
        if arr[i][j]==1:
            print('# ',end='')
        else:
            print('0 ',end='')
    print()
