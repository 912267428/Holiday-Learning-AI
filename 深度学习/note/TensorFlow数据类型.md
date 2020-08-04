**List:**
python自带的列表。

**np.array:**
numpy的数据类型，可以存放很大的数据，很方便的进行操作。但是不支持深度学习。

**tf.Tensor:**
tensorflow的数据类型。为了方便学习在很多方面刻意与numpy的array相近。
tensor：rank>2
支持：int，float，double，bool，string

## 不同类型的数据：

tf.constant() 函数。不表示常量的意思。来自tensorflow1.0版本。在现在版本中就表示一个tensor的意思

1.直接给一个数会自动确定类型。如果输入数字（eg.1、2）自动为int32。如果带小数点则自动为float32
![tensor_自动确定类型](photo\数据类型1.jpg)
2.可以通过传入dtype参数的值以手动确定数据类型。当输入的数值与类型冲突时将报错。
![](photo\数据类型2.jpg)
3.还有bool和string也支持：
![](photo\数据类型3.jpg)

## Tensor常用的属性：

1.**device**属性:返回类型为string。返回当前**tensor**所在设备的名字。
	将tensor在cpu和gpu上互相转移可以调用cpu()、gpu()
![](photo\常用属性1.jpg)
2.将tensor转化成numpy的数据类型使用numpy()方法：

3.tensor的维度属性：ndim
![](photo\常用属性2.jpg)

4.判断一个东西是不是tensor：tf.is_tensor（）
![](photo\常用属性3.jpg)


