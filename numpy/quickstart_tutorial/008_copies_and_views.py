# -*- coding: utf-8 -*-
import numpy

a = numpy.arange(12)
# 没有复制，仅增加引用
b = a
b.shape = 3, 4  # 改变
b is a  # True

c = a.view()
c is a  # False
c.base is a  # True
c.flags.owndata  # False

c.shape = 2, 6  # a don't change
c[0, 4] = 1234  # change

# slicing returns view
s = a[:, 1: 3]
# s = 10  # not change a
s[:] = 10  # change a
print a

# 深复制
d = a.copy()
d is a  # False
d.base is a  # False
d[0, 0] = 9999  # not change
