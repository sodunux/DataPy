import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tushare as ts


class DataGet:
    def __init__(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置

    def Get_k_data(self, code):
        df = ts.get_k_data(code, ktype='W')
        #df['volume'] = df['volume'] / 30000
        # df.drop(['code'],axis=1)
        # df=df.set_index(['date'])
        # print(df)
        df.to_csv(code + '.csv')
        df.plot()
        plt.show()
        return df

    def Get_hist_data(self, code):
        df = ts.get_hist_data(code)
        df.to_csv(code + '.csv')
        df.plot()
        plt.show()
        return df

    def Get_stock_basics(self):
        df = ts.get_stock_basics()
        df.to_csv('stock_basics.csv')
        return df

    def Get_index(self):
        df = ts.get_index()
        df.to_csv('index.csv')
        return df

    def Get_profit_data(self):
        # 获取分配预案
        df = ts.profit_data(top=60)
        df = df.sort_values(by=['shares'], ascending=False)
        print(df)

    def Get_new_stocks(self):
        # 获取新股数据
        df = ts.new_stocks()
        #df = df.sort_values(by=['shares'], ascending=False)
        print(df)

    def Get_industry_classified(self):
        dt = ts.get_industry_classified()
        dt.to_csv('行业分类.csv')
        print(dt)

    def Get_concept_classified(self):
        dt = ts.get_concept_classified()
        dt.to_csv('概念分类.csv')
        print(dt)

    def Get_area_classified(self):
        dt = ts.get_area_classified()
        dt.to_csv('地域分类.csv')
        print(dt)

    def Get_st_classified(self):
        dt = ts.get_st_classified()
        dt.to_csv('风险警示.csv')
        print(dt)

    def Get_sz50s(self):
        dt = ts.get_sz50s()
        # print(dt)
        dt.to_csv('上证50成分股.csv')
        print(dt)

    def Get_terminated(self):
        dt = ts.get_terminated()
        dt.to_csv('终止上市.csv')
        print(dt)

    def Get_report_data(self, year, mouth):
        dt = ts.get_report_data(year, mouth)
        dt.to_csv('业绩报告' + '.csv')
        print(dt)

    def Get_deposit_rate(self):
        dt = ts.get_deposit_rate()
        dt.to_csv('存款利率.csv')
        print(dt)

    def Get_loan_rate(self):
        dt = ts.get_loan_rate()
        dt.to_csv('贷款利率.csv')
        print(dt)

    def Get_money_supply(self):
        dt = ts.get_money_supply()
        dt.to_csv('货币供应量.csv')
        print(dt)

    def Get_money_supply_bal(self):
        dt = ts.get_money_supply_bal()
        dt.to_csv('货币供应量(年底余额).csv')
        print(dt)

    def Get_gdp_year(self):
        dt = ts.get_gdp_year()
        dt.to_csv('年度GDP.csv')
        print(dt)

    def Get_gdp_quarter(self):
        dt = ts.get_gdp_quarter()
        dt.to_csv('季度GDP.csv')
        print(dt)

    def Get_cpi(self):
        dt = ts.get_cpi()
        dt.to_csv('居民消费价格指数cpi.csv')
        print(dt)

    def Get_latest_news(self):
        dt = ts.get_latest_news()
        dt.to_csv('最新新闻.csv')
        print(dt)


if __name__ == '__main__':
    dg = DataGet()
    # dg.Get_k_data('600000')
    # dg.Get_hist_data('600000')
    # dg.Get_index()
    # dg.Get_profit_data()
    # dg.Get_new_stocks()
    # dg.Get_industry_classified()
    # dg.Get_concept_classified()
    # dg.Get_area_classified()
    # dg.Get_st_classified()
    # dg.Get_sz50s()
    # dg.Get_terminated()
    # dg.Get_gdp_quarter()
    dg.Get_latest_news()
