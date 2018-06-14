# -*- coding:utf-8 -*-

from public.Http_Request import HttpRequest
from public.Kaptcha import get_kaptcha
from public.Config_Read import ReadConfig
import json


class GetLogin:

    def __init__(self):
        self.http_request = HttpRequest()
        self.kaptcha = get_kaptcha()
        rc = ReadConfig("config.ini")
        self.userName = rc.get_bs("USERNAME")
        self.passWord = rc.get_bs("PASSWORD")
        self.uuid = rc.get_bs("UUID")
        self.userType = rc.get_bs("USERTYPE")
        self.appVersion = rc.get_bs("appVersion")
        self.url = "http://"+rc.get_bs("IP")+":"+rc.get_bs("PORT")+rc.get_api_url("login")
        # print(self.url)

    def get_request(self):
        data = {
                "userName": self.userName,
                "passWord": self.passWord,
                "uuid": self.uuid,
                "kaptcha": self.kaptcha,
                "userType": self.userType,
                "appVersion": self.appVersion
                }
        header = {'Content-Type': 'application/json'}
        res = self.http_request.post(self.url, header, data)
        # res = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        print(res)
        return res

    def get_session(self):
        data = self.get_request()
        return data['responseData']['sessionID']


if __name__ == '__main__':
    print(GetLogin().get_session())