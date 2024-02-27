import pandas as pd

from BaoFangRisk.BFBarra import BaseRiskFactor
from BaoFangRisk.BFData import BFPortfolio
from BaoFangRisk.BFFetch import BaseFetch
from BaoFangRisk.BFUtil import bf_util_code_change_format
from BaoFangRisk.BFUtil.logs import bf_util_log_info
"""
BaoFangRisk: 风险因子的上层封装 支持
1. 底层风险因子的数据访问
2. 高可用的数据结构
3. 可视化实现
"""


class BaoFangRisk(object):
    def __init__(self, risk_factor: BaseRiskFactor, data_fetch: BaseFetch):
        self.risk_factor = risk_factor
        self.data_fetch = data_fetch

    """
    市场相关
    """

    def get_factor_return(self, start_date, end_date, factors=None, universe='whole_market', method='implicit'):
        """
        获取因子收益率
        :return:
        """
        bf_util_log_info("BaoFangRisk 正在获取因子收益率")
        return self.risk_factor.get_factor_return(start_date, end_date, factors, universe, method)

    """
    投资组合相关
    """

    def get_risk_expose(self, portfolio: BFPortfolio):
        """
        获取投资组合每个因子的暴露度
        :return:
        """
        bf_util_log_info("BaoFangRisk 正在计算投资组合的因子暴露")
        ret = {}
        dates = portfolio.date
        for date in dates:
            codes = portfolio.code(date)
            positions = portfolio.position(date)
            day_stock_risk_expose = self.risk_factor.get_factor_exposure(codes, date, date)
            ret[date] = day_stock_risk_expose.multiply(list(positions.values()), axis="index").sum()
        return pd.DataFrame(data=ret).T

    def get_benchmark_risk_expose(self, portfolio: BFPortfolio):
        """
        获取投资组合基准组合的暴露度
        :return:
        """
        bf_util_log_info("BaoFangRisk 正在计算benchmark的因子暴露")
        ret = {}
        dates = portfolio.date
        benchmark = portfolio.benchmark
        for date in dates:
            # 获取指数成分股 计算暴露
            print(benchmark, date)
            index_weights = self.data_fetch.index_weights(benchmark, date)
            codes = list(index_weights.keys())
            day_stock_risk_expose = self.risk_factor.get_factor_exposure(codes, date, date)
            ret[date] = day_stock_risk_expose.multiply(list(index_weights.values), axis="index").sum()
        return pd.DataFrame(data=ret).T

    def get_revenue_contribution(self):
        """
        获取投资组合每个因子的收益贡献度
        :return:
        """
        pass

    def get_risk_contribution(self):
        """
        获取投资组合每个因子的风险贡献度
        :return:
        """
        pass

    def get_index_proportion(self, portfolio: BFPortfolio, index: list = None):
        """
        获取投资组合各个指数的占比
        :return:
        """
        bf_util_log_info("BaoFangRisk 正在计算投资组合的指数分布")
        if index is None:
            index = ['000300', '000905', '000016']
        index = list(map(lambda code: bf_util_code_change_format(code, market='index'), index))
        ret = {}
        dates = portfolio.date
        for date in dates:
            day_ret = {}
            codes = portfolio.code(date)
            print(codes)
            positions = portfolio.position(date)
            # 查询每个股票属于哪个指数
            # todo：后期对于常用数据 考虑增量维护一个sqlite本地数据库
            for index_code in index:
                # print(index_code, date)
                index_weights = self.data_fetch.index_weights(index_code, date)
                day_ret[index_code] = sum(
                    list(map(lambda code: positions[code] if code in index_weights else 0, codes)))
            day_ret['other'] = 1 - sum(list(map(lambda iindex_code: day_ret[iindex_code], index)))
            ret[date] = day_ret
        return pd.DataFrame(data=ret).T
