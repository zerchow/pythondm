# -*- coding: utf-8 -*-
# ADF平稳性检验
from statsmodels.tsa.stattools import adfuller
import numpy

print adfuller(numpy.random.rand(100))
