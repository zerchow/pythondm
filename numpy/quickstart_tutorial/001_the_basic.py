# -*- coding: utf-8 -*-
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
