# -*- coding:utf-8 -*-
from public.Excel_Operation import GetExcel
from public.Http_Request import HttpRequest
from public.Data_Operation import GetData
from jsonpath_rw import parse


class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.get_excel = GetExcel()
        self.get_request = HttpRequest()
        self.get_data = GetData()

    # 通过caseId去获取该case的整行数据
    def get_depend_line_data(self):
        depend_line_data = self.get_excel.get_row_data_by_content(self.case_id)
        return depend_line_data

    # 执行以来测试，获取结果
    def run_depend(self):
        row_id = self.get_excel.get_row_id(self.case_id)
        url = self.get_data.get_request_url(row_id)
        method = self.get_data.get_request_method(row_id)
        header = self.get_data.get_request_header(row_id)
        data = self.get_data.get_request_data(row_id)
        expect = self.get_data.get_expect(row_id)
        res = self.get_request.run(method, url, header, data)
        return res

    # 获得依赖数据
    def get_depend_key_value(self, row):
        depend_data = self.get_data.get_depend_data(row)
        respond_data = self.run_depend()
        jsonpath_expr = parse(depend_data)
        depend_key_value = jsonpath_expr.find(respond_data)
        depend_key_value = [match.value for match in depend_key_value]
        # print(depend_key_value)
        return depend_key_value[0]


if __name__ == '__main__':
    a = DependData('app01')
    print(a.get_depend_key_value(2))



