from BaoFangRisk.BFBarra.base import BaseRiskFactor
import rqdatac

rqdatac.init()


class RiceQuantBarra(BaseRiskFactor):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def risk_factor_info(self):
        """
        风险因子名称
        :return:
        """
        style_factor = ['momentum', 'beta', 'book_to_price', 'earnings_yield', 'liquidity',
                        'size', 'residual_volatility', 'non_linear_size', 'leverage', 'growth']
        market_factor = ['comovement', ]
        industry_factor = ['银行', '计算机', '环保', '商贸零售', '电力设备', '建筑装饰', '建筑材料',
                           '农林牧渔', '电子', '交通运输', '汽车', '纺织服饰', '医药生物', '房地产', '通信', '公用事业', '综合',
                           '机械设备', '石油石化', '有色金属', '传媒', '家用电器', '基础化工', '非银金融', '社会服务', '轻工制造',
                           '国防军工', '美容护理', '煤炭', '食品饮料', '钢铁']

        return {
            'style_factor': style_factor,
            'market_factor': market_factor,
            'industry_factor': industry_factor
        }

    def get_factor_exposure(self, order_book_ids, start_date, end_date, factors=None):
        """
        获取一组股票的因子暴露度
        :return:
        """
        data = rqdatac.get_factor_exposure(order_book_ids, start_date, end_date, factors, model='v2')
        return data

    def get_factor_return(self, start_date, end_date, factors=None, universe='whole_market', method='implicit'):
        """
        获取因子收益率
        :param universe:基准指数。默认为全市场('whole_market')， 可选沪深 300 ('000300.XSHG'),中证 500 ('000905.XSHG')、中证 800（'000906.XSHG'）
        :param method:计算方法 （ 1 ） 。默认为 'implicit'（隐式因子收益率） ，可选'explicit'（显式风格因子收益率）
        :return:
        """
        data = rqdatac.get_factor_return(start_date, end_date, factors, universe=universe, method=method, model='v2')
        return data

    def get_specific_return(self, order_book_ids, start_date, end_date):
        """
        获取一组股票的特异收益率
        :return:
        """
        data = rqdatac.get_specific_return(order_book_ids, start_date, end_date, model='v2')
        return data

    def get_factor_covariance(self, date, horizon='daily'):
        """
        获取因子协方差
        :param horizon:预测期限。默认为日度（ 'daily'），可选月度（ 'monthly'）或季度（'quarterly'）
        :return:
        """
        data = rqdatac.get_factor_covariance(date, horizon=horizon, model='v2')
        return data

    def get_specific_risk(self, order_book_ids, start_date, end_date, horizon='daily'):
        """
         获取一组股票的特异波动率
        :param horizon:预测期限。默认为日度（ 'daily'），可选月度（ 'monthly'）或季度（'quarterly'）
        :return:
        """
        data = rqdatac.get_specific_risk(order_book_ids, start_date, end_date, horizon=horizon, model='v2')
        return data
