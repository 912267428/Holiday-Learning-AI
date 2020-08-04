## TensorFlow:

先用版本2.x。
旧版本1.X完全完全忘记就行了。

### TensorFlow的优点：

1）GPU加速：对于矩阵的乘法有很好的加速效果。
2）自动求导。
	无论多么复杂，TensorFlow都可以自动求导。

```python
import tensorflow as tf 
# 创建4个张量
a = tf.constant(1.)
b = tf.constant(2.)
c = tf.constant(3.)
w = tf.constant(4.)

with tf.GradientTape() as tape:# 构建梯度环境
	tape.watch([w]) # 将w加入梯度跟踪列表
	# 构建计算过程
	y = a * w**2 + b * w + c
# 求导
[dy_dw] = tape.gradient(y, [w])
print(dy_dw)
```

3）有神经网络的API。可以非常方便的完成神经网络的搭建。

