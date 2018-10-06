import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts
from datetime import datetime


class TsPy:
    def __init__(self):
        pass

    def get_k_data(self, code):
        # 日期，股票代码，开盘价，收盘价，最高价，最低价，成交量
        dat = ts.get_k_data(code)
        #dat = dat.set_index('date')
        dat.index = pd.to_datetime(dat['date'])  # 设置索引为交易日期
        dat = dat.drop(['date', 'code'], axis=1)  # 删除Code栏
        dat = dat.drop(['open', 'high', 'low'], axis=1)
        #dat.to_csv(code + ".csv")
        dat = (dat - dat.min()) / (dat.max() - dat.min())  # 数据归一化
        dat = dat + 1  # 整体加一
        dat['volume'] = dat['volume'] - 0.5  # 成交量减一
        dat.plot(title=code)
        print(dat.describe())
        plt.grid()
        plt.show()

    def get_hist_data(self, code):
        # 日期，开盘价，最高价，收盘价，最低价，成交量，价格变动
        # 涨跌幅，5日均价，10日均价，20日均价
        # 5日均量，10日均量，20日均量
        dat = ts.get_hist_data(code, start="2008-01-01", end="2018-09-28")
        dat = dat.drop(['price_change', 'p_change'], axis=1)
        dat.index = pd.to_datetime(dat.index)

        # dat = dat.drop(['date', 'code'], axis=1)  # 删除Code栏
        #dat = dat.drop(['open', 'high', 'low'], axis=1)
        # dat = (dat - dat.min()) / (dat.max() - dat.min())  # 数据归一化
        # dat = dat + 1  # 整体加一
        # dat['volume'] = dat['volume'] - 0.5  # 成交量减一
        dat.plot(title=code)
        # print(dat.describe())
        # plt.grid()
        plt.show()

    def demo(self):
        dat = pd.read_csv('money_suppy.csv')
        dat.index = pd.to_datetime(dat['month'])
        dat.drop(['month'], axis=1)
        print(dat)
        dat.plot()
        plt.show()


if __name__ == '__main__':
    pdat = TsPy()
    # pdat.get_k_data('600000')
    # pdat.get_hist_data('600000')
    pdat.demo()
