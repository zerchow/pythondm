# -*- coding: utf-8 -*-

import numpy

# numpy的操作都是基于每个元素的
a = numpy.array([20, 30, 40, 50])
b = numpy.arange(4)

c = a - b

b **= 2

d = 10 * numpy.sin(a)

e = a < 35

A = numpy.array([
    [1, 1],
    [0, 1]
])
B = numpy.array([
    [2, 0],
    [3, 4]
])
# 一般乘法
C = A * B

# 矩阵乘法
D = A.dot(B)
E = numpy.dot(A, B)

f = numpy.ones((2, 3), dtype=int)
g = numpy.random.random((2, 3))
# 直接修改原来数组
a *= 3
# 不同类型相加会出错
# a += b

h = numpy.ones(3, dtype=numpy.int32)
i = numpy.linspace(0, numpy.pi, 3)
# 除非不修改，自动向上提升
j = h + i
k = numpy.exp(j * 1j)

# 累积和，最小值，最大值
l = numpy.random.random((2, 3))
print l.sum()
print l.min()
print l.max()

# 通过axis控制
m = numpy.arange(12).reshape(3, 4)
# 按列求和
print m.sum(axis=0)
# 按行求最小
print m.min(axis=1)
# 按行累积
print m.cumsum(axis=1)
