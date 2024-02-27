from BaoFangRisk.BFFetch.base import BaseFetch
import rqdatac
rqdatac.init()

"""
基于米框数据查询
"""


class RiceQuantFetch(BaseFetch):
    def __init__(self):
        pass

    def index_weights(self, order_book_id, date=None):
        return rqdatac.index_weights(order_book_id, date)
