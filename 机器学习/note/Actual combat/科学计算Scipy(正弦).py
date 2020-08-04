# coding=utf-8
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt


def func(x, p):
    A, K, theta = p
    return A * np.sin(2 * np.pi * K * x * theta)


def residuals(p, y, x):
    return y - func(x, p)


x = np.linspace(0, -2 * np.pi, 100)
A, K, theta = 10, 0.34, np.pi / 6
y0 = func(x, [A, K, theta])
y1 = y0 + 2 * np.random.randn(len(x))

p0 = [7, 0.2, 0]

plsq = leastsq(residuals, p0, args=(y1, x))
print("真实:", [A, K, theta])
print("拟合：", plsq[0])

plt.plot(x, y0, label="真实数据")
plt.plot(x, y1, label="噪声数据")
plt.plot(x, func(x, plsq[0]), label="拟合数据")
plt.legend()
plt.show()
