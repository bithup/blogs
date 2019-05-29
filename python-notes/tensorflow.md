## resources and tuorials

- [TensorFlow-2.0-Tutorials](https://github.com/dragen1860/TensorFlow-2.x-Tutorials)
- [验证码识别](https://github.com/kerlomz/captcha_trainer)

## 常用api

- tf.zeros()

```python
tf.zeros(
    shape,
    dtype=tf.float32,
    name=None
)
```

- tf.Variable()

```python
tf.Variable(initializer,name)
```

- tf.random_uniform((4, 4), minval=low,maxval=high,dtype=tf.float32)))返回4*4的矩阵，产生于low和high之间，产生的值是均匀分布的

- tf.multiply()两个矩阵对应的数相乘
- tf.matmul()两个矩阵做矩阵乘法
- tf.square()求平方
- tf.reduce_mean()平均值最小化

## tf.train