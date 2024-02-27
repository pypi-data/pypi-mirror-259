class BaseFetch(object):
    def index_weights(self, order_book_id, date=None):
        """
        获取指数成分
        :return:
        """
        raise NotImplementedError
