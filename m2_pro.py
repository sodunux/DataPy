import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
filename = open('货币供应量.csv', encoding='gbk')
dt = pd.read_csv(filename)
dt = dt[['m2', 'm1', 'm0', 'sd', 'qm', 'cd']]
dt = dt[0:170]
dt.index = np.arange(170, 0, -1)
dt = dt.astype('float64')
dt.plot()
# plt.plot(dt.index,dt.values)
plt.show()
