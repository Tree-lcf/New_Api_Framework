# -*- coding:utf-8 -*-

import json


class GetJson:

    def __init__(self, json_path, json_key):
        self.path = json_path
        self.key = json_key
        self.data = self.read_data()

    # 读取Json文件内容
    def read_data(self):
        with open(self.path, encoding='utf-8') as fp:
            self.data = json.load(fp)
            return self.data

    # 读取某个关键字的值
    def get_value(self):
        value = self.data[self.key]
        return value


if __name__ == '__main__':
    filename = '../config/httpdata.json'
    key = "getQuotationList"
    opers = GetJson(filename, key)
    print(opers.get_value())