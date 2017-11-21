#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

mu=100
sigma=20

# 样本数量
x=mu+sigma*np.random.randn(20000)
# bins显示有几个直方,normed是否对数据进行标准化
plt.hist(x,bins=100,color='green',normed=True)
plt.show()