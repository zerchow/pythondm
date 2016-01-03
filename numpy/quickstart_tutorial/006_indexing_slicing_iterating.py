# -*- coding: utf-8 -*-
import numpy

# one-dimensional arrays can be indexed, sliced and iterated over, much like lists and other python sequences

a = numpy.arange(10) ** 3

print a
print a[2]
print a[2: 5]

# 改变值
a[0: 6: 2] = -1000
# 反转
a = a[:: -1]

for i in a:
    print i, i ** (1 / 3.)

def f(x, y):
    return 10 * x + y

# 多维数组
b = numpy.fromfunction(f, (5, 4), dtype=int)
print b
print b[2, 3]  # 参数其实是元组

# 每一行的第二列
print b[0:5, 1]
print b[:, 1]

# 第二和第三行
print b[1: 3, :]

# 当某一维被省略时，相当于取全部
print b[-1]  # 相当于b[-1, :]

# 省略号用于简化
# 假设x为五维
# x[1, 2, ...]相当于x[1, 2, :, :, :]
# x[..., 3]相当于x[:, :, :, :, 3]
# x[4, ..., 5, :]相当于x[4, :, :, 5, :]

c = numpy.array([
    [
        [0, 1, 2],
        [10, 12, 13]
    ],
    [
        [100, 101, 102],
        [110, 112, 113]
    ]
])
print c.shape
print c[1, ...]  # c[1, :, :], c[1]
print c[..., 2]  # c[:, :, 2]

# 迭代时依照第一维
for row in b:
    print row

# flat用于铺平所有元素，可用于迭代
for element in b.flat:
    print element
print [element for element in b.flat]
