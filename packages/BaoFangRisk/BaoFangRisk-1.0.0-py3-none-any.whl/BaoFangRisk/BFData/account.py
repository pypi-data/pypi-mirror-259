import requests
import json
"""
基于内部分仓系统的账号封装

支持各种维度的查询以及控制

对于基金管理人而言 所有的数据都应该从Account中去获取，所有的操作都应该在Account层面去执行

可以把风险组件  交易组件  可视化组件都放在这
"""

"""
收益性的包括年化收益率、净利润、总盈利、总亏损、有效年化收益率、资金使用率。

风险性主要包括胜率、平均盈亏比、最大回撤比例、最大连续亏损次数、最大连续盈利次数、持仓时间占比、贝塔。

综合性指标主要包括风险收益比，夏普比例，波动率，VAR，偏度，峰度等
"""


class BFAccount(object):
    def __init__(self, account, password):
        self.url_http = r'https://tradeweb.hzyotoy.com/stapi'
        self.is_login = False
        self.account = account
        self.password = password
        self.order_header = None
        self.accessToken = None

    def login(self):
        login_request = {
            "userName": self.account,
            "password": self.password
        }

        login_headers = {'content-type': "application/json",
                         'deviceID': '100100100'}
        login_req = requests.post(self.url_http + "/Login/doLogin",
                                  data=json.dumps(login_request),
                                  headers=login_headers)
        login_msg = json.loads(login_req.text)

        if 'msg' in login_msg and login_msg['msg'] == '登录失败':
            print('登录失败')
        else:
            self.accessToken = login_msg['data']['accessToken']
            # self.sub_account = login_msg['data']['id']

            self.order_header = {
                'content-type': "application/json",
                'Authorization': 'Bearer ' + self.accessToken,

            }
            self.is_login = True
            print('登录成功')

    def load_history(self):
        """
        从子账户接口获取所有历史信息
        :return:
        """
        pass

    @property
    def positions(self):
        # 当前持仓信息
        pos_request = {
            "contractCode": "",
            "pageSize": 5000,
            "pageIndex": 0
        }

        pos_headers = {
            'content-type': "application/json",
            'Authorization': 'Bearer ' + self.accessToken

        }

        r_pos = requests.post(self.url_http + "/api/position/pageList",
                              data=json.dumps(pos_request),
                              headers=pos_headers)

        positions_json = json.loads(r_pos.text)

        if positions_json['data'] is None:
            positions = {}
        else:
            positions = positions_json['data']['data']
            print(positions)
            positions = {item['contractCode']: int(item['marketValue']) for item in positions}
        return positions


    def beta(self):
        """
        beta比率 组合的系统性风险
        """
        pass

    def alpha(self):
        """
        alpha比率 与市场基准收益无关的超额收益率
        """
        pass