# -*- coding: utf-8 -*-
import pandas

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pandas.read_table('movielens/users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pandas.read_table('movielens/ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pandas.read_table('movielens/movies.dat', sep='::', header=None, names=mnames, engine='python')

# print users.head()
# print ratings.head()
# print movies.head()
#    user_id gender  age  occupation    zip
# 0        1      F    1          10  48067
# 1        2      M   56          16  70072
# 2        3      M   25          15  55117
# 3        4      M   45           7  02460
# 4        5      M   25          20  55455
#    user_id  movie_id  rating  timestamp
# 0        1      1193       5  978300760
# 1        1       661       3  978302109
# 2        1       914       3  978301968
# 3        1      3408       4  978300275
# 4        1      2355       5  978824291
#    movie_id                               title                        genres
# 0         1                    Toy Story (1995)   Animation|Children's|Comedy
# 1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
# 2         3             Grumpier Old Men (1995)                Comedy|Romance
# 3         4            Waiting to Exhale (1995)                  Comedy|Drama
# 4         5  Father of the Bride Part II (1995)                        Comedy

data = pandas.merge(pandas.merge(ratings, users), movies)

# 按性别计算每部电影的平均得分
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print mean_ratings.head()
# gender                                F         M
# title
# $1,000,000 Duck (1971)         3.375000  2.761905
# 'Night Mother (1986)           3.388889  3.352941
# 'Til There Was You (1997)      2.675676  2.733333
# 'burbs, The (1989)             2.793478  2.962085
# ...And Justice for All (1979)  3.828571  3.689024

# 过滤掉评分数据不够250条的电影
ratings_by_title = data.groupby('title').size()
# print ratings_by_title.head()
# title
# $1,000,000 Duck (1971)            37
# 'Night Mother (1986)              70
# 'Til There Was You (1997)         52
# 'burbs, The (1989)               303
# ...And Justice for All (1979)    199
active_titles = ratings_by_title.index[ratings_by_title > 250]
mean_ratings = mean_ratings.ix[active_titles]

# 女性观众最喜欢的电影，对F列降序排列
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print top_female_ratings.head()
# gender                                                     F         M
# title
# Close Shave, A (1995)                               4.644444  4.473795
# Wrong Trousers, The (1993)                          4.588235  4.478261
# Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)       4.572650  4.464589
# Wallace & Gromit: The Best of Aardman Animation...  4.563107  4.385075
# Schindler's List (1993)                             4.562602  4.491415

# 找出男性和女性观众分歧最大的电影，增加一列存放平均分只差
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
# 按diff排序，根据前面，可得到分歧最大且女性观众更喜欢的电影
sorted_by_diff = mean_ratings.sort_values(by='diff')
# 对排序结果反序，得到男性观众更喜欢的电影
sorted_by_diff_man = sorted_by_diff[::-1]

# 如果不考虑性别因素找出分歧最大的电影，则可以计算数据的方差或标准差
ratings_std_by_title = data.groupby('title')['rating'].std()
ratings_std_by_title = ratings_std_by_title.ix[active_titles]
ratings_std_by_title = ratings_std_by_title.sort_values(ascending=False)
print ratings_std_by_title.head()
