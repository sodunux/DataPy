import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'

if __name__ == "__main__":

    dat = np.random.randint(100, size=100)
    dat = pd.Series(dat)
    plt.plot(dat, label="测试")
    plt.legend()
    plt.show()
