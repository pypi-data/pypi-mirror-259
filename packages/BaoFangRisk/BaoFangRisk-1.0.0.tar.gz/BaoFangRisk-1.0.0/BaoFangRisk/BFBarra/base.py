class BaseRiskFactor(object):
    """
    风险因子基类
    """
    #
    # def __init__(self, *args, **kwargs):
    #     pass

    @property
    def risk_factor_info(self):
        """
        风险因子名称
        :return:
        """
        raise NotImplementedError

    def get_factor_exposure(self, order_book_ids, start_date, end_date, factors=None):
        """
        获取一组股票的因子暴露度
        :return:
        """
        raise NotImplementedError

    def get_factor_return(self, start_date, end_date, factors=None, universe='whole_market', method='implicit'):
        """
        获取因子收益率
        :param universe:基准指数。默认为全市场('whole_market')， 可选沪深 300 ('000300.XSHG'),中证 500 ('000905.XSHG')、中证 800（'000906.XSHG'）
        :param method:计算方法 （ 1 ） 。默认为 'implicit'（隐式因子收益率） ，可选'explicit'（显式风格因子收益率）
        :return:
        """
        raise NotImplementedError

    def get_specific_return(self, order_book_ids, start_date, end_date):
        """
        获取一组股票的特异收益率
        :return:
        """
        raise NotImplementedError

    def get_factor_covariance(self, date, horizon= 'daily'):
        """
        获取因子协方差
        :param horizon:预测期限。默认为日度（ 'daily'），可选月度（ 'monthly'）或季度（'quarterly'）
        :return:
        """
        raise NotImplementedError

    def get_specific_risk(self, order_book_ids, start_date, end_date, horizon= 'daily'):
        """
         获取一组股票的特异波动率
        :param horizon:预测期限。默认为日度（ 'daily'），可选月度（ 'monthly'）或季度（'quarterly'）
        :return:
        """
        raise NotImplementedError
