**1.Norm:**

<img src="photo\数据统计1.jpg" style="zoom:67%;" />
使用tf.norm函数中ord参数指定翻数。

二翻数：

![](photo\数据统计2.jpg)

**最大值，最小值，均值：**
使用函数：reduce_min/max/mean:	还可以用axis参数指定维度：
![](photo\数据统计3.jpg)

**最大值，最小值的位置：**
使用函数argmax与argmin：axis参数指定维度，默认为0；
![](photo\数据统计4.jpg)

**tensor的比较：**
tf.equal函数

![](photo\数据统计5.jpg)



