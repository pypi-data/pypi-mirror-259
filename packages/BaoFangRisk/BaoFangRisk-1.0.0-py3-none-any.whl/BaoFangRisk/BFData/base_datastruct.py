import datetime
import json
import os
import statistics
import webbrowser
from abc import abstractmethod
from copy import copy, deepcopy
from functools import lru_cache

import numpy as np
import pandas as pd
from dateutil import parser

try:
    from pyecharts import Bar, Grid, Kline
except:
    from pyecharts.charts import Kline, Bar, Grid


"""
同一份数据 保留基础属性的同时 在不同工况  应该具备不同的特性
通过 基础数据 + 方法封装  展示这些特性

作为一个基础数据类 应该提供以下功能
1. 多维度的查询
2. 可视化
3. 数理统计
"""


class BaseData(object):
    # def __init__(
    #         self,
    #         data,
    #         ):
    #     pass

    def analyze(self):
        pass

    def plot(self):
        pass