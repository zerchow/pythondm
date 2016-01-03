# -*- coding: utf-8 -*-
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html
import numpy

the_basic = numpy.array([
    [1, 0, 0],
    [0, 1, 2]
])

# ndarray.ndim，数组的维数，秩
print the_basic.ndim

# ndarray.shape，每一维的大小
print the_basic.shape

# ndarray.size，总数目，shape每个数的乘积
print the_basic.size

# ndarray.dtype，元素类型
print the_basic.dtype

# ndarray.itemsize，元素占字节数
print the_basic.itemsize, the_basic.dtype.itemsize

# ndarray.data，原始数据
print '<', the_basic.data, '>'

a = numpy.arange(15).reshape(3, 5)
print a, a.itemsize
