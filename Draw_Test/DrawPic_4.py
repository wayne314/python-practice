#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(1000)
y=x+np.random.randn(1000)*0.5
plt.scatter(x,y,s=5,marker='<')# s表示面积，marker表示图形
plt.show()