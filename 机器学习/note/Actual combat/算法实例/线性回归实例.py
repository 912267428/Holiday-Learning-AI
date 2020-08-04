import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

#加载糖尿病数据集
d_X, d_Y = datasets.load_diabetes(return_X_y=True)
d_X = d_X[:,np.newaxis,2]

#划分数据集与训练集
d_X_train = d_X[:-20]
d_X_test = d_X[-20:]
d_Y_train = d_Y[:-20]
d_Y_test = d_Y[-20:]

#创建线性回归对象
regr = linear_model.LinearRegression()

#使用训练集训练模型
regr.fit(d_X_train,d_Y_train)

#使用测试集进行预测
d_Y_pred = regr.predict(d_X_test)

#系数：
print('coefficients:\n', regr.coef_)
#均方误差：
print('Mean squared error: %.2f'
      % mean_squared_error(d_Y_test, d_Y_pred))
#确定系数：1为完美预测
print('Coefficient of determination: %.2f'
      % r2_score(d_Y_test, d_Y_pred))
#绘图输出
plt.scatter(d_X_test, d_Y_test,  color='black')
plt.plot(d_X_test, d_Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()