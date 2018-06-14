# -*- coding:utf-8 -*-

from public.Excel_Operation import GetExcel
from config import test_data_config
from public.Json_Operation import GetJson


class GetData:
    def __init__(self):
        self.get_excel_data = GetExcel()
        # self.session = GetLogin().get_session()

    # 获取excel行数
    def get_case_num(self):
        return self.get_excel_data.get_lines()

    # 获取case name
    def get_case_name(self, row):
        col = test_data_config.get_caseName_col()
        casename = self.get_excel_data.get_cell_value(row, col)
        return casename

    # 获取是否执行testcase
    def get_is_run(self, row):
        col = test_data_config.get_runStatus_col()
        if self.get_excel_data.get_cell_value(row, col) == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取headerfile路径
    def get_header_file(self, row):
        col = test_data_config.get_header_file_col()
        header = self.get_excel_data.get_cell_value(row, col)
        return header

    # 获取header json key
    def get_header_key(self, row):
        col = test_data_config.get_header_key_col()
        header_file = self.get_excel_data.get_cell_value(row, col)
        return header_file

    # 获取request header data
    def get_request_header(self, row):
        header = GetJson(self.get_header_file(row), self.get_header_key(row)).get_value()
        return header

    # 获取http请求方式
    def get_request_method(self, row):
        col = test_data_config.get_method_col()
        request_method = self.get_excel_data.get_cell_value(row, col)
        return request_method

    # 获取host地址
    def get_host(self, row):
        col = test_data_config.get_host_col()
        host = self.get_excel_data.get_cell_value(row, col)
        return host

    # 获取url
    def get_url(self, row):
        col = test_data_config.get_url_col()
        url = self.get_excel_data.get_cell_value(row, col)
        return url

    # 获取完整路径
    def get_request_url(self, row):
        request_url = self.get_host(row)+self.get_url(row)
        return request_url

    # 获取body file路径
    def get_body_file(self, row):
        col = test_data_config.get_body_file_col()
        body_file = self.get_excel_data.get_cell_value(row, col)
        return body_file

    # 获取body key值
    def get_body_key(self, row):
        col = test_data_config.get_body_key_col()
        body_key = self.get_excel_data.get_cell_value(row, col)
        return body_key

    # 获得发送request的data
    def get_request_data(self, row):
        data = GetJson(self.get_body_file(row), self.get_body_key(row)).get_value()
        return data

    # 获取预期值
    def get_expect(self, row):
        col = test_data_config.get_expect_col()
        expect = self.get_excel_data.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 写入数据
    def write_result(self, row, value):
        col = test_data_config.get_result_col()
        result = self.get_excel_data.write_data(row, col, value)

    def get_depend_caseID(self, row):
        col = test_data_config.get_depend_case_col()
        depend_caseID = self.get_excel_data.get_cell_value(row, col)
        return depend_caseID

    def get_depend_data(self, row):
        col = test_data_config.get_depend_data_col()
        depend_data = self.get_excel_data.get_cell_value(row, col)
        return depend_data

    def get_depend_key(self, row):
        col = test_data_config.get_depend_key_col()
        depend_key = self.get_excel_data.get_cell_value(row, col)
        return depend_key


if __name__ == '__main__':
    opers = GetData()
    print(opers.get_expect(2))

