# -*- coding:utf-8 -*-

from utility.Http_Request import HttpRequest
from utility.Excel_Operation import GetExcel
from utility.Depend_Operation import DependData
from utility.Mail import SendMail
from utility.GetLog import MyLog

import json
import unittest
import paramunittest

quotations_xls = utility.get_xls("productCase.xlsx", "getProductInfo")

class GetRun:
    def __init__(self):
        self.http_request = HttpRequest()
        self.data = GetData()
        self.pass_list = []
        self.fail_list = []
        self.send_mail = SendMail()

    def go_on_run(self):
        num = self.data.get_case_num()
        for i in range(1, num):
            casename = self.data.get_case_name(i)
            # print(casename)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            header = self.data.get_request_header(i)
            data = self.data.get_request_data(i)
            expect = self.data.get_expect(i)
            depend_case = self.data.get_depend_caseID(i)
            depend_data = self.data.get_depend_data(i)
            depend_key = self.data.get_depend_key(i)
            if is_run:
                if depend_case is not '':
                    depend = DependData(depend_case)
                    depend_key_value = depend.get_depend_key_value(i)
                    data[depend_key] = depend_key_value
                    if self.data.get_body_key(i) is not 'login':
                        header_patch = {'sessionID': depend_key_value}
                        header = dict(header, **header_patch)
                res = self.http_request.run(method, url, header, data)
                res = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=4)
                # print(res)
                if expect in res:
                    self.data.write_result(i, 'Pass')
                    self.pass_list.append(casename)
                    print('Testing Pass, and filed result in excel already')

                else:
                    self.data.write_result(i, 'Fail')
                    self.fail_list.append(casename)
                    print('Testing Fail')


if __name__ == "__main__":
    run = GetRun()
    run.go_on_run()
