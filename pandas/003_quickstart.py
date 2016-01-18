# -*- coding: utf-8 -*-
import pandas

# names1880 = pandas.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
# print names1880.head()
#         name sex  births
# 0       Mary   F    7065
# 1       Anna   F    2604
# 2       Emma   F    2003
# 3  Elizabeth   F    1939
# 4     Minnie   F    1746
# print names1880.groupby('sex').head()
#           name sex  births
# 0         Mary   F    7065
# 1         Anna   F    2604
# 2         Emma   F    2003
# 3    Elizabeth   F    1939
# 4       Minnie   F    1746
# 942       John   M    9655
# 943    William   M    9533
# 944      James   M    5927
# 945    Charles   M    5348
# 946     George   M    5126
# print names1880.groupby('sex').births.head()
# 0      7065
# 1      2604
# 2      2003
# 3      1939
# 4      1746
# print names1880.groupby('sex').births.sum()
# sex
# F     90993
# M    110493
# Name: births, dtype: int64

# 将所有数据组装到一个DataFrame里面，并加上一个year字段
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'names/yob%d.txt' % year
    frame = pandas.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pandas.concat(pieces, ignore_index=True)

# 不管性别，统计每年出生的男女
total_births = pandas.pivot_table(data=names, values='births', index='year', columns='sex', aggfunc=sum)
# print total_births.tail()
# sex         F        M
# year
# 2006  1896468  2050234
# 2007  1916888  2069242
# 2008  1883645  2032310
# 2009  1827643  1973359
# 2010  1759010  1898382
import matplotlib.pyplot as plt
# total_births.plot(title='Total births by sex and year')
# plt.show()

# 指定婴儿数相对于总出生数的比例
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births / births.sum()
    return group
# print names.groupby(['year', 'sex']).head()  # 按年份和性别统计名字的数量
names = names.groupby(['year', 'sex']).apply(add_prop)
# 有效性检查，prop总和是否足够接近于1
import numpy
# sum_prop = names.groupby(['year', 'sex']).prop.sum()
# print sum_prop
# print numpy.allclose(sum_prop, 1)

# 计算每对sex/year组合的前1000个名字
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[: 1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
# print top1000.head()
# 其他方法
# pieces = []
# for year, group in names.groupby(['year', 'sex']):
#     pieces.append(group.sort_values(by='births', ascending=False)[: 1000])
# top1000 = pandas.concat(pieces, ignore_index=True)

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
# print boys.head()
#                  name sex  births  year      prop
# year sex
# 1880 M   942     John   M    9655  1880  0.087381
#          943  William   M    9533  1880  0.086277
#          944    James   M    5927  1880  0.053641
#          945  Charles   M    5348  1880  0.048401
#          946   George   M    5126  1880  0.046392

# 生成按year和name统计的总出生数透视表
# total_births = pandas.pivot_table(data=top1000, values='births', index='year', columns='name', aggfunc=sum)
# subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
# plt.show()

# 上图表示给小孩起常见名字越来越少
# 验证，计算最流行的1000个名字所占比例
# 按year和sex进行聚合
table = pandas.pivot_table(data=top1000, values='prop', index='year', columns='sex', aggfunc=sum)
# table.plot(title='Sum of table1000.prop by year and sex', yticks=numpy.linspace(0, 1.2, 13))
# plt.show()
# 名字多样性出现了增长，因为前1000项的比例下降
# 还可以计算占总出生人数前50%的不同名字的数量（不好计算）
# 试图考虑2010年男孩名字
# df = boys[boys.year == 2010]
# prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
# 找出0.5应该插入的位置
# pos = prop_cumsum.searchsorted(0.5)
# print type(pos), pos  # 116 + 1 = 117，而1900年才25
def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().searchsorted(q) + 1

# diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
# print diversity
# year  sex
# 1880  F       [38]
#       M       [14]
# diversity = diversity.unstack('sex')
# print diversity
# sex       F      M
# year
# 1880   [38]   [14]
# 现在这个DataFrame拥有两个时间序列，每个性别各一个，按年度索引
# diversity = diversity.astype(int)
# diversity.plot(title="Number of popular names in top 50%")
# plt.show()
# 女孩名字的多样性比男孩高，而且变得越来越高

# 将全部出生数据在年度、性别以及末字母上进行聚合
get_last_letter = lambda x: x[-1]
last_letter = names.name.map(get_last_letter)
last_letter.name = 'last_letter'
table = pandas.pivot_table(data=names, values='births', index=last_letter, columns=['sex', 'year'], aggfunc=sum)
# print table
# 选出具有一定代表性的三年
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# print subtable
# sex               F                      M
# year           1910    1960    2010   1910    1960    2010
# last_letter
# a            108376  691247  670605    977    5204   28438
# b               NaN     694     450    411    3912   38859
# c                 5      49     946    482   15476   23125
# 按总出生数对表进行规范化处理，计算各性别各末字母占各年总出生人数的比例
# letter_prop = subtable / subtable.sum().astype(float)
# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
# plt.show()
# 以字母n结尾的男孩名字出现了显著的增长

# 对完整表按年和性别进行处理，并在男孩名字中选取几个字母，最后进行转置以便将各个列做成时间序列
# letter_prop = table / table.sum().astype(float)
# dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
# dny_ts.plot()
# plt.show()

# 变成女孩名字的男孩名字
all_names = top1000.name.unique()
mask = numpy.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
# print lesley_like  # ['Leslie' 'Lesley' 'Leslee' 'Lesli' 'Lesly']
# 利用这个结果过滤其他名字，按名字分组计算出生数以查看相对频率
filtered = top1000[top1000.name.isin(lesley_like)]
# filtered_sum = filtered.groupby('name').births.sum()
# print filtered_sum
# name
# Leslee      1082
# Lesley     35022
# Lesli        929
# Leslie    370429
# Lesly      10067
# Name: births, dtype: int64
# 按性别和年度进行聚合，并按年度进行处理
table = pandas.pivot_table(data=filtered, values='births', index='year', columns='sex', aggfunc=sum)
table = table.div(table.sum(1), axis=0)
table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()
# 得出各年度使用lesley型名字的男女比例
