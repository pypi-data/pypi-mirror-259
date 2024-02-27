headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}


def _select_bond_market_code(code):

    if code[0:3] in ['101', '104', '105', '106', '107', '108', '109',
                        '111', '112', '114', '115', '116', '117', '118', '119',
                        '123', '127', '128',
                        '131', '139', ]:
        return 0
    else:
        return 1

def _select_market_code(code):
    """
    1- sh
    0 -sz
    """
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0


def _select_index_code(code):
    """
    1 - sh
    0 - sz
    """
    code = str(code)
    if code[0] == '3':
        return 0
    return 1

def get_stock_market(code):
    return 'SH' if _select_market_code(code) == 1 else 'SZ'

def get_index_market(code):
    return 'SH' if _select_index_code(code) == 1 else 'SZ'


def _select_type(frequence):
    if frequence in ['day', 'd', 'D', 'DAY', 'Day']:
        frequence = 9
    elif frequence in ['w', 'W', 'Week', 'week']:
        frequence = 5
    elif frequence in ['month', 'M', 'm', 'Month']:
        frequence = 6
    elif frequence in ['Q', 'Quarter', 'q']:
        frequence = 10
    elif frequence in ['y', 'Y', 'year', 'Year']:
        frequence = 11
    elif str(frequence) in ['5', '5m', '5min', 'five']:
        frequence, type_ = 0, '5min'
    elif str(frequence) in ['1', '1m', '1min', 'one']:
        frequence, type_ = 8, '1min'
    elif str(frequence) in ['15', '15m', '15min', 'fifteen']:
        frequence, type_ = 1, '15min'
    elif str(frequence) in ['30', '30m', '30min', 'half']:
        frequence, type_ = 2, '30min'
    elif str(frequence) in ['60', '60m', '60min', '1h']:
        frequence, type_ = 3, '60min'

    return frequence

'''
沪市
010xxx 国债
001×××国债现货；
110×××120×××企业债券；
129×××100×××可转换债券；
201×××国债回购；
310×××国债期货；
500×××550×××基金；
600×××A股；
700×××配股；
710×××转配股；
701×××转配股再配股；
711×××转配股再转配股；
720×××红利；
730×××新股申购；
735×××新基金申购；
737×××新股配售；
900×××B股。
深市
第1位	第二位	第3-6位	含义
0	0	XXXX	A股证券
0	3	XXXX	A股A2权证
0	7	XXXX	A股增发
0	8	XXXX	A股A1权证
0	9	XXXX	A股转配
1	0	XXXX	国债现货
1	1	XXXX	债券
1	2	XXXX	可转换债券
1	3	XXXX	国债回购
1	7	XXXX	原有投资基金
1	8	XXXX	证券投资基金
2	0	XXXX	B股证券
2	7	XXXX	B股增发
2	8	XXXX	B股权证
3	0	XXXX	创业板证券
3	7	XXXX	创业板增发
3	8	XXXX	创业板权证
3	9	XXXX	综合指数/成份指数
北交
8   2   XXXX    北交所优先股
8   3   XXXX    北交所普通股
8   7   XXXX    北交所普通股
8   8   XXXX    北交所公开发行
深市A股票买卖的代码是以000打头，如：顺鑫农业：股票代码是000860。
B股买卖的代码是以200打头，如：深中冠B股，代码是200018。
中小板股票代码以002打头，如：东华合创股票代码是002065。
创业板股票代码以300打头，如：探路者股票代码是：300005
'''

def for_sz(code):
    """深市代码分类
    Arguments:
        code {[type]} -- [description]
    Returns:
        [type] -- [description]
    """

    if str(code)[0:2] in ['00', '30', '02']:
        return 'stock_cn'
    elif str(code)[0:2] in ['39']:
        return 'index_cn'
    elif str(code)[0:2] in ['15', '16']:
        return 'etf_cn'
    elif str(code)[0:3] in ['101', '104', '105', '106', '107', '108', '109',
                            '111', '112', '114', '115', '116', '117', '118', '119',
                            '123', '127', '128',
                            '131', '139', ]:
        # 10xxxx 国债现货
        # 11xxxx 债券
        # 12xxxx 可转换债券

            # 123
            # 127
        # 12xxxx 国债回购
        return 'bond_cn'

    elif str(code)[0:2] in ['20']:
        return 'stockB_cn'
    else:
        return 'undefined'

def for_sh(code):
    if str(code)[0] == '6':
        return 'stock_cn'
    elif str(code)[0:3] in ['000', '880']:
        return 'index_cn'
    elif str(code)[0:2] in ['51', '58']:
        return 'etf_cn'
    # 110×××120×××企业债券；
    # 129×××100×××可转换债券；
    # 113A股对应可转债 132
    elif str(code)[0:3] in ['102', '110', '113', '120', '122', '124',
                            '130', '132', '133', '134', '135', '136',
                            '140', '141', '143', '144', '147', '148']:
        return 'bond_cn'
    else:
        return 'undefined'

def for_bj(code):
    return 'stock_cn'
