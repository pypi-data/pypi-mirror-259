import finhack.library.log as Log
from runtime.constant import *
import runtime.global_var as global_var
from finhack.market.astock.astock import AStock
import time
from finhack.factor.default.factorManager import factorManager
from finhack.factor.default.factorAnalyzer import factorAnalyzer
from finhack.factor.default.factorPkl import factorPkl
from finhack.library.mydb import mydb
import pandas as pd


class DefaultTestmodule():
    #finhack testmodule run
    def __init__(self):
        pass
    def run(self):
        Log.logger.debug("----%s----" % (__file__))
        Log.logger.debug("this is Testmodule")
        Log.logger.debug("vendor is default")
        print(self.args)
        while True:
            time.sleep(1)
            Log.logger.debug(".")
        
        
    def run2(self):
        print(self.args)
        print('run2')
        stock_list=AStock.getStockCodeList(strict=False, db='tushare')
        print(stock_list)
        
        
    def run3(self):
        factorAnalyzer.alphalens("pe_0")
        
    def run4(self):
        factors=factorManager.getFactors(['ADOSC_0','AD_0','APO_0','AROONDOWN_0','ARRONUP_0','pe_0','alpha101_012','alpha101_013'],start_date='20150101',end_date="20230101")
        print(factors)
        
        
    def run5(self):
        # import dask.dataframe as dd
        # path = '/data/code/finhack/examples/demo-project/data/factors/single_factors_parquet/*.parquet'
        # ddf = dd.read_parquet(path)
        # print(ddf)

        # ddf_single = dd.read_parquet('/data/code/finhack/examples/demo-project/data/factors/single_factors_parquet/turnoverRatef_0.parquet')
        # print(ddf_single)

        df=factorManager.getFactors(factor_list=['open','close'])
        # 首先定义你想要选取的索引列表
        df=df.reset_index()
        print(df)
        # 使用 .loc 方法选取这些索引对应的行
        df = df[df.trade_date=='20240118']
        df = df[df.trade_date=='20240118']


        print(df)
        
    def run6(self):
        print('test')
        pass
    
    
    def run7(self):
        max_num = 30
        # 从数据库中获取数据
        df = mydb.selectToDf('SELECT a.ts_code, trade_date, pe, pb, ps, total_mv, industry, market FROM astock_price_daily_basic a LEFT JOIN astock_basic b ON a.ts_code=b.ts_code', 'tushare')
    
        # 确保 'trade_date' 是 datetime 类型
        df['trade_date'] = pd.to_datetime(df['trade_date'])
    
        # 将需要聚合的列转换为数值类型，并处理无法转换的数据
        agg_columns = ['pe', 'pb', 'ps', 'total_mv']
        for col in agg_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
        # 删除在转换过程中产生的NaN值所在的行，以便聚合函数可以正常工作
        df.dropna(subset=agg_columns, inplace=True)
    
        # 计算每个交易日的统计量
        stats = df.groupby('trade_date')[agg_columns].agg(['median', 'mean', 'min', 'max'])
    
        # 由于多级列索引，我们需要创建一个新的列索引
        stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
        
        # 重置索引以便于合并
        stats.reset_index(inplace=True)
    
        # 将统计数据合并到原始 DataFrame 中
        df_neutral = df.copy()
        for col in agg_columns:
            for stat in ['median', 'mean', 'min', 'max']:
                df_neutral = df_neutral.merge(stats[['trade_date', f'{col}_{stat}']], on='trade_date', how='left')
                df_neutral[f'{col}_score_{stat}'] = df_neutral[col] / df_neutral[f'{col}_{stat}']
    
        # 计算综合得分
        for stat in ['median', 'mean', 'min', 'max']:
            df_neutral[f'score_{stat}'] = df_neutral[[f'{col}_score_{stat}' for col in agg_columns]].mean(axis=1)
    
        # 对每个行业和市场进行分组，选择得分最接近统计量的股票
        selected_stocks = []
        groups = df_neutral.groupby(['industry', 'market'])
    
        for _, group in groups:
            for stat in ['median', 'mean', 'min', 'max']:
                # 确保至少返回一个结果
                n_stocks = max(1, max_num // (len(groups) * 4))  # 除以4因为有4种统计量
                selected_group = group.nsmallest(n=n_stocks, columns=f'score_{stat}', keep='all')
                selected_stocks.extend(selected_group['ts_code'].drop_duplicates().tolist())
    
        # 如果选出的股票不足max_num支，可以从剩余股票中按得分选择补充
        if len(selected_stocks) < max_num:
            remaining_stocks = df_neutral[~df_neutral['ts_code'].isin(selected_stocks)]
            for stat in ['median', 'mean', 'min', 'max']:
                top_stocks = remaining_stocks.nsmallest(n=(max_num - len(selected_stocks)) // 4, columns=f'score_{stat}')
                selected_stocks.extend(top_stocks['ts_code'].drop_duplicates().tolist())
    
        # 去除可能的重复并限制数量为max_num
        selected_stocks = list(dict.fromkeys(selected_stocks))[:max_num]
    
        # 创建一个包含选出股票的新DataFrame
        selected_df = df[df['ts_code'].isin(selected_stocks)]
    
        # 打印选出的股票列表和DataFrame
        print(selected_stocks)
        print(selected_df)
