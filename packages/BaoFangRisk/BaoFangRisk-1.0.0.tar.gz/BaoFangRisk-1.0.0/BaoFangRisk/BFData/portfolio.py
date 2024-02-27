from BaoFangRisk.BFData.base_datastruct import BaseData
from BaoFangRisk.BFUtil import bf_util_code_change_format


class BFPortfolio(BaseData):
    def __init__(self, positions: dict, benchmark: str):
        self.positions = {}
        for date in positions.keys():
            self.positions[date] = {}
            for code in positions[date].keys():
                self.positions[date][bf_util_code_change_format(code)] = positions[date][code]
        self.benchmark = bf_util_code_change_format(benchmark, market='index')

    @property
    def date(self):
        return list(self.positions.keys())

    def position(self, date):
        return self.positions[date]

    def code(self, date):
        return list(self.positions[date].keys())
