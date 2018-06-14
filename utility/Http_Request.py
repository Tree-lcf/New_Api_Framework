# -*- coding:utf-8 -*-

import requests


class HttpRequest:

    def post(self, url, header, data):
        res = requests.post(url, headers=header, json=data)
        # print(res.status_code)
        return res.json()

    def get(self,url, header, data):
        res = requests.get(url, headers=header, json=data)
        # print(res.status_code)
        return res.json()

    def run(self, method, url, header, data):
        if method == 'post':
            res = self.post(url, header, data)
        else:
            res = self.get(url, header, data)
        return res


if __name__ == "__main__":
    run = HttpRequest()
    method1 = "post"
    url1 = "http://58.214.236.155:12480/login"
    header1 = {"Content-Type": "application/json"}
    data1 = {"uuid": "1234qwer", "appVersion": "3.15", "passWord": "Jfpt123456", "kaptcha": "454862", "userType": "2", "userName": "Ajsbc"}
    print(run.run(method1, url1, header1, data1))
