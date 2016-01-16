# -*- coding: utf-8 -*-
import json

path = 'usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]

print len(records)
print records[0]
print records[0]['tz']

# 对时区进行计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[: 10]
# 第一种，遍历计数
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
from collections import defaultdict
def get_counts2(sequence):
    '''利用标准库'''
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts
counts = get_counts(time_zones)
print counts['America/New_York']
counts = get_counts2(time_zones)
print counts['America/New_York']
print 'time_zone length: ', len(time_zones)
# 计数前十位
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for (tz, count) in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
print top_counts(counts)
# 利用标准库取前十位
from collections import Counter
counts = Counter(time_zones)
print counts.most_common(10)

# 第二种，利用pandas
import pandas
import matplotlib.pyplot as plt
import numpy
frame = pandas.DataFrame(records)
# print frame  # [3560 rows x 18 columns]
# print frame['tz'][: 10]
tz_counts = frame['tz'].value_counts()
print tz_counts[: 10]
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
# tz_counts[: 10].plot(kind='barh')
# plt.show()

# 分离浏览器信息
results = pandas.Series([x.split()[0] for x in frame['a'].dropna()])
print results[: 5]
print results.value_counts()[: 8]

# 统计windows和非windows
cframe = frame[frame['a'].notnull()]
operating_system = numpy.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print operating_system[: 5]
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print agg_counts[: 10]
# 选出最常出现的时区
indexer = agg_counts.sum(1).argsort()  # 根据行数构造一个间接索引数组
print indexer[: 10]
count_subset = agg_counts.take(indexer)[-10:]  # 按照这个顺序截取最后10行
print count_subset
count_subset.plot(kind='barh', stacked=True)
plt.show()
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
print normed_subset
normed_subset.plot(kind='barh', stacked=True)
plt.show()
