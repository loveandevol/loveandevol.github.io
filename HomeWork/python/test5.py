#!/usr/bin/python

import numpy as np
#1.创建两个数组arr1 = [1,2,3,4]和arr2 = [5,6,7,8]，对这两个数组进行四则运算。\
print("四则运算----------->>>")
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)
#2.创建数组arr3 =［［1, 2, 3, 4］,［4, 5, 6, 7］, ［7, 8, 9, 10］］，将数据数组arr3的形状改为（4,3）并输出。
print("reshape----------->>>")
arr3 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr3.reshape(4,3))
#3.创建两个形状相同的数据，并将这两数组分别进行水平叠放、垂直叠放和深度叠放。
print("叠放----------->>>")
arr1 = np.arange(12).reshape(4,3)
arr2 = np.arange(12).reshape(4,3)
print(np.hstack((arr1,arr2)))
print(np.vstack((arr1,arr2)))
print(np.dstack((arr1,arr2)))
#4.创建数组arr9 = [1,1,5,7,2,8,4]，分别完成排序、去重、总和、均值、标准差、方差、最小值、最大值的统计。
print("统计运算----------->>>")
arr9 = np.array([1,1,5,7,2,8,4])
arr9.sort()
print("排序后:", arr9, "\n", "去重:", np.unique(arr9), "\n", "总和:", np.sum(arr9), "\n",
        "均值:", np.mean(arr9), "\n", "标准差:", np.std(arr9), "\n", "方差:", np.var(arr9), "\n",
        "最小值:", np.min(arr9), "\n", "最大值:", np.max(arr9))
