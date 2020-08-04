# coding=utf-8
# 直线的拟合
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

#采样点
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])

#需要拟合的函数和误差
def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y,s):
    print(s)
    return func(p,x)-y

#线的初始值
p0=[100,2]
s="测试最小二乘法"
Para = leastsq(error,p0,args=(Xi,Yi,s))
k,b = Para[0]
print(k,'\n',b)

#图像显示\
plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="wc",linewidth=3)
x = np.linspace(0,10,1000)
y = k*x+b
plt.plot(x,y,color="orange",label="fit",linewidth=2)
plt.legend()
plt.show()