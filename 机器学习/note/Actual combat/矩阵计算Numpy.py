import numpy as np
import time
import math

# 创建数组
a = np.array([1,2,3,4])
b = np.array([[1,2,3,3],[4,5,6,6],[7,8,9,9]],dtype=np.float)
b.shape = 4,3  #转换  行列
print(b)
b[0][0] = 20
print(b.dtype)

#
a = np.arange(0,1,0.1)#0到1，步长为0.1
print(a)

b = np.linspace(1,100,10)#等比数列  (第三个参数是生成多少个)
print(b)

#数组元素的存取
a = np.arange(10)
print(a)
print(a[2])
print(a[2:5])
print(a[2:-1])

#矩阵运算
a = np.arange(12).reshape(4,3)
b = np.arange(12).reshape(3,4)
c = np.dot(a,b)
print(c)

#文件存取
a = np.arange(0,12,0.5).reshape(4,-1)
np.savetxt("./a.txt",a,fmt="%d",delimiter=",") #只保存整数和以逗号作为分隔
b = np.loadtxt("./a.txt",delimiter=",")
print(b)