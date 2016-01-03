# -*- coding: utf-8 -*-
import numpy

#
# indexing with arrays of indices
#
a = numpy.arange(12) ** 2
print a

i = numpy.array([1, 1, 3, 8, 5])
print a[i]

j = numpy.array([
    [3, 4],
    [9, 7]
])
print a[j]

palette = numpy.array([
    [0, 0, 0],
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 255]
])
image = numpy.array([
    [0, 1, 2, 0],
    [0, 3, 4, 0]
])
print palette[image]

b = numpy.arange(12).reshape(3, 4)
i = numpy.array([
    [0, 1],
    [1, 2]
])
j = numpy.array([
    [2, 1],
    [3, 3]
])
# i跟j的shape要一致
print b[i, j]

print b[i, 2]

print b[i, :]

print b[:, j]

# 预先组合
l = [i, j]
print b[l]

# 不可行
s = numpy.array([i, j])
# print b[s]

# 另一种
print b[tuple(s)]
