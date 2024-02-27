"""
code名称适配
"""
import numpy as np
from collections import Iterable
from BaoFangRisk.BFUtil.base import (get_index_market,get_stock_market)

def bf_util_code_change_format(code, format='rq', market='stock'):
    '''
    股票数据格式转换，任意输入，输出为指定格式，如果为6位代码，需要指定为stock-index，或者指定sh-sz
    '''
    
    # 聚宽/米框 股票代码格式 '600000.XSHG'
    # 掘金股票代码格式 'SHSE.600000'
    # Ifind、Tushare、Wind股票代码格式 '600000.SH'
    # 天软股票代码格式 'SH600000'
    
    if isinstance(code, str):
        code2=[code]
        ls=0
    elif isinstance(code, list): 
        pass
        code2=code
        ls=1
    res_=[]
    for code in code2: 
        if len(code) == 6:
            #code='000001'
            if market in ['stock','STOCK']:
                res=code+'.'+get_stock_market(code) 
            elif market in ['index','INDEX','etf','ETF']:
                res=code+'.'+get_index_market(code) 
            elif market in ['sh','SH']:
                res=code+'.SH'
            elif market in ['sz','SZ']:
                res=code+'.SZ'
                
        if len(code) == 8:
            # code='SH600000'
            res=code[2:]+'.'+code[:2]
        if len(code) == 9:
            res=code
        if len(code) == 11:
            #code='SHSE.000001'
            if code[0] in ["S"]:
                if code.split(".")[0][-1]=='E':
                    res=code.split(".")[1]+'.SH'
                else:
                    res=code.split(".")[1]+'.SZ'
            else:
                if code.split(".")[1][-1]=='E':
                    res=code.split(".")[0]+'.SH'
                else:
                    res=code.split(".")[0]+'.SZ'
    
        if format in ['jq','joinquant','JQ','JOINQUANT']:
            if res[-1] =='H':
                res=code.split(".")[0]+'.XSHG'
            elif res[-1] =='Z':
                res=code.split(".")[0]+'.XSHE'
        if format in ['rq','ricequant','RQ','RICEQUANT']:
            if res[-1] =='H':
                res=code.split(".")[0]+'.XSHG'
            elif res[-1] =='Z':
                res=code.split(".")[0]+'.XSHE'
            
        elif format in ['ifind', 'iFind','ts','TS','Tushare','tushare','TUSHAREA']:
            pass
    res_.append(res)
    
    if ls==0:
        return res_[0]
    else:
        return res_


def bf_util_code_tostr(code):
    """
    explanation:
        将所有沪深股票从数字转化到6位的代码,因为有时候在csv等转换的时候,诸如 000001的股票会变成office强制转化成数字1,
        同时支持聚宽股票格式,掘金股票代码格式,Wind股票代码格式,天软股票代码格式,Ifind股票代码格式

    params:
        * code ->
            含义: 代码
            类型: str
            参数支持: []
    """
    if isinstance(code, int):
        return "{:>06d}".format(code)
    if isinstance(code, str):
        # 聚宽股票代码格式 '600000.XSHG'
        # 掘金股票代码格式 'SHSE.600000'
        # Wind股票代码格式 '600000.SH'
        # 天软股票代码格式 'SH600000'
        # Ifind股票代码格式 '600000.SH'
        if len(code) == 6:
            return code
        if len(code) == 8:
            # 天软数据
            return code[-6:]
        if len(code) == 9:
            return code[:6]
        if len(code) == 11:
            if code[0] in ["S"]:
                return code.split(".")[1]
            return code.split(".")[0]
        raise ValueError("错误的股票代码格式")
    if isinstance(code, list) or isinstance(code, Iterable):
        return [bf_util_code_tostr(item) for item in code]


def bf_util_code_tolist(code, auto_fill=True):
    """
    explanation:
        将转换code==> list

    params:
        * code ->
            含义: 代码
            类型: str
            参数支持: []
        * auto_fill->
            含义: 是否自动补全(一般是用于股票/指数/etf等6位数,期货不适用) (default: {True})
            类型: bool
            参数支持: [True]
    """

    if isinstance(code, str):
        if auto_fill:
            return [bf_util_code_tostr(code)]
        else:
            return [code]

    elif isinstance(code, list):
        if auto_fill:
            return [bf_util_code_tostr(item) for item in code]
        else:
            return [item for item in code]
