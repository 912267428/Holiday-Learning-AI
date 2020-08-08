## Broadvasting:

将一个tensor的维度扩张但是不会复制该tensor的数据但是可以完成相应维度的计算。

**使用范围：**先从小维度匹配，匹配后即使小维度的tensor没有大维度的某些意思也可以通过Broadvasting完成运算。默认维度为1对所有的数据都是使用的。

**好处**：1.代码简洁。
			2.不需要人为的扩大内存。

![](photo\Broadcasting1.jpg)
当两个运算可以broadcast时不需要调用broadcast_to函数也户自动调用以支持运算。

手动调用broadast函数：
![](photo\Broadcasting2.jpg)