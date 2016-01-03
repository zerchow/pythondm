# -*- coding: utf-8 -*-
import numpy

a = numpy.array([2, 3, 4])
b = numpy.array((2, 3, 4))
c = numpy.array([
    (1.5, 2, 3),
    (4, 5, 6)
])
d = numpy.array([
    [1, 2],
    [3, 4]
], dtype=complex)

# 全为零的数组
e = numpy.zeros((3, 4))

# 全为一的数组
f = numpy.ones((2, 3, 4), dtype=numpy.int16)

# 随机，未初始化的数组
g = numpy.empty((2, 3))

# 一维序列
h = numpy.arange(10, 30, 5)
i = numpy.arange(0, 2, 0.3)

# 为了控制个数
j = numpy.linspace(0, 2, 9)
k = numpy.linspace(0, 2 * numpy.pi, 100)
l = numpy.sin(k)

