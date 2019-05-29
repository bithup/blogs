## numpy notes

- 创建一维数组

```python
np.array([1,2,3,4,5])
np.array((1,2,3,4,5))
#一些快捷的初始化方法
np.zeros((5))
np.ones((5))
np.random.random((5))
np.arange(5)
np.linspace(0, 2*np.pi, 5)
#创建二维数组
np.zeros(2, 3)
#查看数组属性
mynp.dtype
mynp.shape
mynp.itemsize
mynp.ndim
mynp.nbytes
```

- 矩阵乘法和一般乘法

```python
mynp1 = np.array([1,2,3,4,5])

mynp2 = np.array([1,2,3,4,5])
mynp1 * mynp2
mynp1.dot(mynp2)
```


- numpy一维数组和二维数组切片

```python
# 一维数组切片
mynp[a:b]
# 二维数组切片
mynp[x:y, m:n]
mynp[:, n]
mynp[::m, ::n]
```

## numpy.random模块

- numpy.random.rand(d0, d1, ..., dn) 生成形状为（d0,d1,...,dn)的[0,1)数组，dtype=float64
- numpy.random.random_integers(low, high=None, size=None)  生成size个整数，取值区间为[low, high], 若没有输入参数high则取值区间为[1, low]，注意这里左右都是闭区间
- [博客](https://www.cnblogs.com/JetReily/p/9398148.html)


## online resources

- [quickstart](https://www.numpy.org/devdocs/user/quickstart.html)
- [SciPy](https://scipy.org/install.html)
- [numpy中文文档](https://www.numpy.org.cn/)

## words

words|explanation|
----|----|
homogeneous|
axes|
coordinates|
indicating|
