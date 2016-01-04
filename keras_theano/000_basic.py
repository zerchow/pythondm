# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD

# 搭建多层感知机

# 模型初始化
model = Sequential()
# 添加输入层（20节点）、第一隐藏层（64节点）的连接
model.add(Dense(20, 64))
# 第一隐藏层用tanh作为激活函数
model.add(Activation('tanh'))
# 使用Dropout防止过拟合
model.add(Dropout(0.5))
# 添加第一隐藏层、第二隐藏层的连接
model.add(Dense(64, 64))
# 第二隐藏层用tanh作为激活函数
model.add(Activation('tanh'))
#
model.add(Dropout(0.5))
# 添加第二隐藏层、输出层的连接
model.add(Dense(64, 1))
# 输出层用sigmoid作为激活函数
model.add(Activation('sigmoid'))

# 定义求解算法
sgd = SGD(lr=0.1, momentum=0.9, decay=1e-6, nesterov=True)
# 编译生成模型，损失函数为平均误差平方和
model.compile(loss='mean_squared_error', optimizer=sgd)

# 训练模型
# model.fit(X_train, y_train, nb_epoch=20, batch_size=16)
# 测试模型
# score = model.evaluate(X_test, y_test, batch_size=16)
