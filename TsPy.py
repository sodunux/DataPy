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

    def get_cpi(self):
        dat=ts.get_cpi()
        dat.index = pd.to_datetime(dat['month'])
        dat = dat.drop(['month'], axis=1)
        dat['cpi']=dat['cpi']/100
        dat=dat['2018':'2008'] #选取时间片
        dat=dat.sort_index() #倒序
        dat['cpi2']=dat['cpi'].cumprod(axis=0) #计算累乘
        dat.to_csv("cpi.csv")
        dat.plot()
        plt.show()


    def money_suppy(self):
        dat = pd.read_csv('money_suppy.csv')
        dat.index = pd.to_datetime(dat['month'])
        dat.drop(['month'], axis=1)
        dat['m2-m1']=dat['m2']-dat['m1']
        dat['m2-m0']=dat['m2']-dat['m0']
        print(dat)
        dat.plot()
        plt.show()

    def cpi_vs_m2(self):
        #此处的计算有误，获得的数据是同比，而本函数计算是环比增长的方法
        dat_cpi = ts.get_cpi()
        dat_m2 = ts.get_money_supply()
        dat_cpi.index=pd.to_datetime(dat_cpi['month'])
        dat_m2.index=pd.to_datetime(dat_m2['month'])
        dat_cpi = dat_cpi['2018':'2008']
        dat_m2 = dat_m2['2018':'2008']
        dat_m2['cpi']=dat_cpi['cpi']
        dat = dat_m2[['m0','m1','m2','cpi']]
        dat = dat.sort_index()
        dat['cpi']= dat['cpi']/100
        dat['cpi'] = dat['cpi'].cumprod(axis=0)
        dat = dat.astype(dtype='float64')
        dat = (dat - dat.min()) / (dat.max() - dat.min())
        dat.plot()
        plt.show()

    def gdp_vs_m2(self):
        dat_cpi = ts.get_cpi()
        dat_m2 = ts.get_money_supply()
        dat_gdp = ts.get_gdp_year()
        dat_gdp.index =pd.to_datetime(dat_gdp['year'], format='%Y')
        dat_gdp=dat_gdp.to_period('A')
        dat_gdp = dat_gdp['gdp']
        dat_gdp = dat_gdp['2017':'2000']
        dat_gdp=dat_gdp.sort_index()
        #dat_gdp = (dat_gdp - dat_gdp.min()) / (dat_gdp.max() - dat_gdp.min())
        dat_cpi.index=pd.to_datetime(dat_cpi['month'])
        dat_m2.index=pd.to_datetime(dat_m2['month'])
        dat_cpi = dat_cpi['2017':'2000']
        dat_m2 = dat_m2['2017':'2000']
        dat_m2['cpi']=dat_cpi['cpi']
        dat = dat_m2[['m0','m1','m2','cpi']]
        dat = dat.sort_index()
        dat['cpi']= dat['cpi']/100
        dat['cpi'] = dat['cpi'].cumprod(axis=0)
        dat = dat.astype(dtype='float64')
        #dat = (dat - dat.min()) / (dat.max() - dat.min())
        dat=dat.resample("AS").first()
        dat= dat.to_period('A')
        #dat=dat.resample("AS").sum()
        dat['gdp']=dat_gdp
        #dat['m2-gdp']=dat['m2']-dat['gdp']
        #dat = (dat - dat.min()) / (dat.max() - dat.min())
        #dat['m2-gdp']=dat['m2']-dat['gdp']
        dat['m0']=dat['m0']/dat['m0']['2000']
        dat['m1']=dat['m1']/dat['m1']['2000']
        dat['m2']=dat['m2']/dat['m2']['2000']
        dat['cpi']=dat['cpi']/dat['cpi']['2000']
        dat['gdp']=dat['gdp']/dat['gdp']['2000']
        dat['m2-gdp']=dat['m2']-dat['gdp']
        dat=dat.drop(['cpi','m0','m1'], axis=1)
        print(dat)
        #dat['m2-gdp'].plot()
        dat.plot()
        plt.show()

    def deposit_vs_loan(self):
        dat_loan=ts.get_loan_rate()
        dat_deposit=ts.get_deposit_rate()
        #dat_loan = dat_loan[dat_loan['loan_type']=="中长期贷款(一至三年)"]
        dat_loan = dat_loan[dat_loan['loan_type']=="短期贷款(六个月以内)"]
        dat_deposit=dat_deposit[dat_deposit['deposit_type']=="活期存款(不定期)"]
        dat_loan.index=pd.to_datetime(dat_loan['date'])
        dat_deposit.index=pd.to_datetime(dat_deposit['date'])
        dat_loan=dat_loan.drop(['date','loan_type'],axis=1)
        dat_deposit=dat_deposit.drop(['date','deposit_type'],axis=1)
        dat_loan=dat_loan['2015':'2000']
        dat_deposit=dat_deposit['2015':'2000']
        dat=dat_loan
        dat['deposit']=dat_deposit['rate']
        dat['loan']=dat['rate']
        dat=dat.drop(['rate'],axis=1)
        dat=dat.dropna()
        dat=dat.astype(dtype='float64')
        dat['loan-deposit']=dat['loan']-dat['deposit']
        print(dat)
        dat.plot()
        plt.show()

    def get_stock_basics(self):
        dat=ts.get_stock_basics()
        print(dat)
        dat.to_csv('股票基本情况.csv',encoding="utf_8_sig")
    
    def get_report_data(self):
        dat=ts.get_report_data(2018,2)
        print(dat)
        dat.to_csv('业绩报告2018年2季度.csv',encoding="utf_8_sig")

    def get_profit_data(self):
        dat=ts.get_report_data(2018,2)
        print(dat)
        dat.to_csv('盈利能力2018年2季度.csv',encoding="utf_8_sig")

    def get_operation_data(self):
        dat=ts.get_operation_data(2018,2)
        print(dat)
        dat.to_csv('营运能力2018年2季度.csv',encoding="utf_8_sig")

    def get_growth_data(self):
        dat=ts.get_growth_data(2018,2)
        print(dat)
        dat.to_csv('成长能力2018年2季度.csv',encoding="utf_8_sig")

    def get_debtpaying_data(self):
        dat=ts.get_growth_data(2018,2)
        print(dat)
        dat.to_csv('偿债能力2018年2季度.csv',encoding="utf_8_sig")

    def get_cashflow_data(self):
        dat=ts.get_cashflow_data(2018,2)
        print(dat)
        dat.to_csv('现金流量2018年2季度.csv',encoding="utf_8_sig")




if __name__ == '__main__':
    pdat = TsPy()
    # pdat.get_k_data('600000')
    # pdat.get_hist_data('600000')
    #pdat.demo()
    #pdat.get_cpi()
    #pdat.gdp_vs_m2()
    #pdat.deposit_vs_loan()
    #pdat.get_stock_basics()
    pdat.get_cashflow_data()
