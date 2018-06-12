# -*- coding:utf-8 -*-

import os
import configparser


proDir = os.path.split(os.path.realpath(__file__))[0]
conf_path = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(conf_path, encoding="utf-8-sig")

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name):
        value = self.cf.get("HEADERS", name)
        return value

    def set_headers(self, name, value):
        self.cf.set("HEADERS", name, value)
        with open(conf_path, 'w+') as f:
            self.cf.write(f)

    def get_url(self, name):
        value = self.cf.get("URL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


if __name__ == '__main__':
    co = ReadConfig()
    print(co.get_http("baseurl"))
    print(co.get_db("host"))
    print(co.get_email("sender"))