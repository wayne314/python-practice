#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,100)
y=x**3
plt.plot(x,y,linestyle='--',color='green',marker='<')
plt.show()