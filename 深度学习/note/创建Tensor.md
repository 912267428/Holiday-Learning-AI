## 创建Tensor：

**1）numpy和list转化得来：**
![](photo\创建tensor1.jpg)
tf.convert_to_tensor()函数可以将numpy的数据类型和list转换成tensor。
	np.ones(m,n):创建一个m行n列的全为1的numpy数组。
	np.zeros(m,n):创建一个m行n列的全为0的numpy数组。
	通过numpy数组转化的tensor的类型是float64的，但是一般需要使用float32位。需要转化。
通过list转换位tensor，该函数可以自动选择类型，比如都是int32则是32int32，一个int类型一个float类型的则转换位float32.

​	tf.constan() 与tf.convert_to_tensor()基本完全相同

**2）tf.zeros()函数可以直接创建一个全0的tensor。该函数接收shape（维度）**
shape：维度  [m,n,z] : 第一行（维）的数据m个、第二行（维）的数据n个、第三行（维）的数据z个。
data：数据 [m,n ]:  m维，每个维度的数据n个。
![](photo\创建tensor2.jpg)
tf.zeros_like()  :  该函数接收一个tensor并以相同的shape创建一个全0的相似tensor：
			tf.zeros_like(a) 相当于 tf.zeros(a.shaoe)
![](photo\创建tensor3.jpg)
同理。tf.ones()和tf.ones_like()也存在。与zeros相比只是将元素数据全改位1.
**3)tf.fill()函数**
fill()函数与zeros函数相识。但是fill()函数需要多传入一个参数，fill()将创建一个指定的shape且数据全部填充为第二个参数的tensor
![](photo\创建tensor4.jpg)

**4) Normal方法:**
随机的初始化方法:（正态分布、均匀分布）
1.tf.random.normal([m,n],mean=X,stddev=U):创建一个shape为(m,n)的tensor且数据值在正态分布N(X,U)中随机取值。(不会去掉在3*σ*范围之外的值)
2.tf.random.truncated_normal([m,n],mean=X,stddev=U).这个函数会去掉在3*σ*范围之外的值所有它对很多模型的优化要好于直接normal的函数。

![](photo\创建tensor5.jpg)

3.tf.random.uniform([m,n],minval=X,maxval=Y)创建一个shape为(m,n)的tensor且数据值在均匀分布X~B(X,Y)中随机取值。也可以指定数据的类型。
![](photo\创建tensor6.jpg)
