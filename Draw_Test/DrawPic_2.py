#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np

y=[20,10,30,25,15,50]
index=np.arange(6)
plt.bar(left=index,height=y,color='blue',width=0.3)
plt.show()