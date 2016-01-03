# -*- coding: utf-8 -*-
import numpy

#
# changing the shape of an array
#
a = numpy.floor(10 * numpy.random.random((3, 4)))

# flatten the array
print a.ravel()

# 直接改变
a.shape = (6, 2)
print a, a.T

# the reshape function returns its argument with a modified shape
# whereas the ndarray.resize method modifies the array itself
a.resize((2, 6))

# -1表示自动计算
a.reshape(3, -1)

#
# stacking together different arrays
#
b = numpy.floor(10 * numpy.random.random((2, 2)))
c = numpy.floor(10 * numpy.random.random((2, 2)))
print b, c, numpy.hstack((b, c)), numpy.vstack((b, c))  # 垂直或者水平组合

# column_stack stacks 1D arrays as columns into 2D array
# it is equivalent to vstack only for 1D arrays
print numpy.column_stack((b, c))  # hstack

d = numpy.array([4., 2.])
e = numpy.array([1., 8.])
print d
print d[:, numpy.newaxis]  # this allows to have 2D columns vector
print 'vstack: ', numpy.vstack((d, e))
print 'column_stack: ', numpy.column_stack((d, e))
print 'column_stack with new: ', numpy.column_stack((d[:, numpy.newaxis], e[:, numpy.newaxis]))
print 'vstack with new: ', numpy.vstack((d[:, numpy.newaxis], e[:, numpy.newaxis]))

# 行拓展
print numpy.r_[1: 4, 0, 4]
# 列拓展
print numpy.c_[1, 4, 5, 7]
