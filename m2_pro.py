import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
filename = open('货币供应量.csv', encoding='gbk')
dt = pd.read_csv(filename)
dt = dt['m2']
dt = dt[0:273]
dt.index = np.arange(273, 0, -1)
dt=dt.astype('float64')
dt.plot()
#plt.plot(dt.index,dt.values)
plt.show()
