# -*- coding: utf-8 -*-
import pandas

s = pandas.Series([1, 2, 3], index=['a', 'b', 'c'])
d = pandas.DataFrame([
    [1, 2, 3],
    [4, 5, 6]
], columns=['a', 'b', 'c'])
d2 = pandas.DataFrame(s)

print d.head()
print d.describe()


# 读Excel
# pandas.read_excel('')
# 读csv
# pandas.read_csv('', encoding='utf-8')
