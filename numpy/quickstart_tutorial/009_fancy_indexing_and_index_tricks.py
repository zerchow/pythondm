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

# time scale
time = numpy.linspace(20, 145, 5)
# 4 time-dependent series
data = numpy.sin(numpy.arange(20)).reshape(5, 4)
print time
print data
# 每一列的最大索引值
ind = data.argmax(axis=0)
print ind

time_max = time[ind]
print time_max

data_max = data[ind, xrange(data.shape[1])]  # data[ind[0], 0], data[ind[1], 1], ...
print data_max

print numpy.all(data.max(axis=0) == data_max)

# 数组赋值
c = numpy.arange(5)
print c
c[[1, 3, 4]] = 0
print c
# 索引重复时赋值也重复
c = numpy.arange(5)
print c
c[[0, 0, 2]] = [1, 2, 3]
print c
# 但是使用+=的时候，不重复
c = numpy.arange(5)
print c
c[[0, 0, 2]] += 1
print c


#
# indexing with boolean arrays
#
a = numpy.arange(12).reshape(3, 4)
b = a > 4
print a
print b
# 返回一维
print a[b]
# 用于赋值
a[b] = 0
print a

# Mandelbrot set
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20):
    '''return a image of the Mandelbrot fractal of size(h, w)'''
    y, x = numpy.ogrid[-1.4: 1.4: h * 1j, -2: 0.8: w * 1j]
    c = x + y * 1j
    z = c
    divtime = maxit + numpy.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z ** 2 + c
        diverge = z * numpy.conj(z) > 2 ** 2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime

# plt.imshow(mandelbrot(400, 400))
# plt.show()

# 通过给定两个维度的一维bool值，用于切片
a = numpy.arange(12).reshape(3, 4)
b1 = numpy.array(
    [False, True, True]
)
b2 = numpy.array(
    [True, False, True, False]
)
print a
print a[b1, :]
print a[b1]
print a[:, b2]
print a[b1, b2]  # 不知道为毛不是返回2*2的


#
# the ix_() function
#
# 用于组合不同的vector

a = numpy.array([
    2, 3, 4, 5
])
b = numpy.array([
    8, 5, 4
])
c = numpy.array([
    5, 4, 6, 8, 3
])
ax, bx, cx = numpy.ix_(a, b, c)
print a.shape, b.shape, c.shape
print ax.shape, bx.shape, cx.shape
result = ax + bx * cx
print result.shape
print result[3, 2, 4]
print a[3] + b[2] * c[4]
