# -*- coding:utf-8 -*-

import xlrd
from xlutils.copy import copy


class GetExcel:

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../test_case_data/api_test_data.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        table = data.sheets()[self.sheet_id]
        return table

    # 获取行数
    def get_lines(self):
        return self.data.nrows

    # 获取某个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据对应的caseid找到对应行的内容
    def get_row_data_by_content(self, case_id):
        row_id = self.get_row_id(case_id)
        row_data = self.get_row_data(row_id)
        return row_data

    # 找到对应内容的行号
    def get_row_id(self, case_id):
        row_id = 0
        cols_data = self.get_col_data()
        for col_data in cols_data:
            if case_id in col_data:
                return row_id
            row_id = row_id + 1

    # 获取某一行的内容
    def get_row_data(self, row_id):
        tables = self.data
        row_data = tables.row_values(row_id)
        return row_data

    # 获取某一列的内容
    def get_col_data(self, col_id=None):
        tables = self.data
        if col_id is not None:
            col_data = tables.col_values(col_id)
        else:
            col_data = tables.col_values(0)
        return col_data


if __name__ == '__main__':
    opers = GetExcel()
    print(opers.get_cell_value(2, 8))