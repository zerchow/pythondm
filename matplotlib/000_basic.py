# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt
# 正常显示中文标签（黑体）
plt.rcParams['font.sans-serif'] = ['SimHei']
# 负号可能显示为方块
plt.rcParams['axes.unicode_minus'] = False

x = numpy.linspace(0, 10, 1000)
y = numpy.sin(x) + 1
z = numpy.cos(x ** 2) + 1

# 设置图像大小
plt.figure(figsize=(8, 4))
# 设置标签、线条颜色、线条大小
plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
plt.plot(x, z, 'b--', label='$\cos x^2+1$')

plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0, 2.2)
plt.legend()

plt.show()
