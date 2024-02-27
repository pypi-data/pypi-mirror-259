# BaoFangRisk

### 介绍
基于Barra的风险组件

### 功能
1. 计算当前持仓的风险因子暴露
2. 组合优化器

### demo

1. 持仓分析demo

```python
import datetime
from datetime import timedelta
import webbrowser

from BaoFangRisk.BFRisk.baofang_risk import BaoFangRisk
from BaoFangRisk.BFBarra import RiceQuantBarra
from BaoFangRisk.BFFetch import RiceQuantFetch
from BaoFangRisk.BFData import BFPortfolio, BFAccount
from BaoFangRisk.BFUtil import *

import os
import numpy as np
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Kline, Bar, Grid, Line, Pie


barra = RiceQuantBarra()
fetch = RiceQuantFetch()
# 构建风险组件
risk = BaoFangRisk(risk_factor=barra, data_fetch=fetch)

# barra风险因子类别
risk_factor_info = barra.risk_factor_info
print("risk_factor:", risk_factor_info)
print("-*"*10)
# 风险因子收益
# 因子收益率在 不同的市场/隐式或者显式计算方法 有不同计算结果
risk_factor_return = risk.get_factor_return(start_date='20230201', end_date='20240210', factors=risk_factor_info['style_factor'])
print("risk_factor_return:", risk_factor_return)
print("-*"*10)

# 模拟一个投资组合仓位
# 所有code在BFPortfolio会自动转化为rq的格式 你可以随心所欲尝试各种格式 如果报错 联系xzr马上修改！
# positions = {
#     '20240207': {
#         '000568': 0.1,
#         '603290': 0.3,
#         '000963': 0.6
#     },
#     '20240208': {
#         '000568': 0.1,
#         '603290': 0.2,
#         '000963': 0.4,
#         '002180': 0.3
#     }
# }

# 或者从账号系统中读取仓位(此处为我司自营分仓系统)
account = BFAccount("your account", 'your password')
account.login()
positions = account.positions
market_value = sum(positions.values())
query_date = datetime.date.today() - timedelta(days=1)
positions = {query_date.strftime("%Y%m%d"): dict(map(lambda x: (x[0], np.round(x[1]/market_value, 4)), positions.items()))}
print(positions)

portfolio = BFPortfolio(positions=positions, benchmark='000300')

# 因子暴露
risk_expose = risk.get_risk_expose(portfolio)
print("risk_expose: ", risk_expose)
print("-*"*10)

# 基准暴露
benchmark_risk_expose = risk.get_benchmark_risk_expose(portfolio)
print("benchmark_risk_expose: ", benchmark_risk_expose)
print("-*"*10)

# 股票成分
index_proportion = risk.get_index_proportion(portfolio)
print("index_proportion: ", index_proportion)
print("-*"*10)

# 可视化
# 简单画下图 这里应该封装到数据结构的基础方法中 把结果推送到web
return_cumsum = risk_factor_return.cumsum()
risk_factor_return_line = Line().add_xaxis(list(return_cumsum.index.strftime("%Y-%m-%d")))
for factor in return_cumsum.columns:
    risk_factor_return_line.add_yaxis(factor, list(np.round(return_cumsum[factor], 3)), label_opts=opts.LabelOpts(is_show=False))
risk_factor_return_line.set_global_opts(title_opts=opts.TitleOpts(title="风险因子收益率"),
                                        legend_opts=opts.LegendOpts(pos_top="5%", pos_right="40%",item_height=7,textstyle_opts=opts.TextStyleOpts(font_size=10)),
                                        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=0))
                                        )

risk_factor_return_bar = (
    Bar()
    .add_xaxis(list(risk_factor_return.columns))
    .add_yaxis("", list(np.round(risk_factor_return.iloc[-1].values, 3)), label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="因子当日收益", pos_left="60%"),
                     legend_opts=opts.LegendOpts(pos_top="48%"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=80, font_size=8)
                                              , splitline_opts={"length": 40})
                     )
)


risk_expose_bar = (
    Bar()
    .add_xaxis(list(risk_expose.columns))
    .add_yaxis("portfolio", list(np.round(risk_expose.iloc[-1].values, 8)), label_opts=opts.LabelOpts(is_show=False),
               itemstyle_opts=opts.ItemStyleOpts(color='black'))
    .add_yaxis("benchmark", list(np.round(benchmark_risk_expose.iloc[-1].values, 8)), label_opts=opts.LabelOpts(is_show=False),
               itemstyle_opts=opts.ItemStyleOpts(color='red'))
    .set_global_opts(title_opts=opts.TitleOpts(title="暴露度", subtitle="最近一日", pos_top="48%"),
                     legend_opts=opts.LegendOpts(pos_top="48%", pos_right="40%"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=80, font_size=8)
                                              , splitline_opts={"length": 40})
                     )
)

index_proportion_pie = (
    Pie()
    .add("指数成分", list(tuple(index_proportion.iloc[-1].items())), radius=[0, 80], center=[600, 400])
    .set_global_opts(legend_opts=opts.LegendOpts(pos_top="60%", pos_left="80%",item_height=7,textstyle_opts=opts.TextStyleOpts(font_size=10)))
)

path_name = 'bf_risk.html'
grid = (Grid()
        .add(risk_factor_return_line, grid_opts=opts.GridOpts(pos_bottom="60%", pos_right="50%"))
        .add(risk_factor_return_bar, grid_opts=opts.GridOpts(pos_bottom="60%", pos_left="70%"))
        .add(risk_expose_bar, grid_opts=opts.GridOpts(pos_top="60%",  pos_right="50%"))
        .add(index_proportion_pie, grid_opts=opts.GridOpts(pos_left='right', pos_top='bottom')) # pos_top="60%",  pos_left="70%"
        .render(path_name))

webbrowser.open(path_name)
```
运行结果
![逻辑框架图](file/positions.jpg) {:width="200px" height="100px"}


2. 组合优化demo