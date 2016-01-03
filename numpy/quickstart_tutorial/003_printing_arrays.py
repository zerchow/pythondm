# -*- coding: utf-8 -*-
import numpy

# 一维
a = numpy.arange(6)
print a

# 二维
b = numpy.arange(12).reshape(4, 3)
print b

# 三维
c = numpy.arange(24).reshape(2, 3, 4)
print c

# 一般numpy会把大的数组省略中间部分打印出来
print numpy.arange(10000)
print numpy.arange(10000).reshape(100, 100)
# 可以禁用这种操作
numpy.set_printoptions(threshold='nan')  # 改为None应该是复原
