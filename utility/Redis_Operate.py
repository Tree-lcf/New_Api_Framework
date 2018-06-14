# -*- coding:utf-8 -*-

import redis
from public.Config_Read import ReadConfig


rc = ReadConfig("config.ini")


class GetRedis:

    """
    redis数据库操作
    """

    def __init__(self):
        """
        初始化
        """
        self.ip = rc.get_redis('IP')
        self.port = rc.get_redis('PORT')
        self.uuid = rc.get_redis('UUID')
        # self.log = MyLog.get_log()
        # self.logger = self.log.get_logger()
        self.conn = None

    def reconnect(self):
        """
        建立连接
        """
        self.conn = redis.StrictRedis(host=self.ip, port=self.port, decode_responses=True)

    def getkaptcha(self):
        """
        获取验证码
        :return:
        """
        value = self.conn.get(self.uuid)
        return value


if __name__ == '__main__':
    test = GetRedis()
    test.reconnect()
    kaptcha = test.getkaptcha()
    print(kaptcha)
