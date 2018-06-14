# -*- coding:utf-8 -*-

from public.Redis_Operate import GetRedis


def get_kaptcha():
    myredis = GetRedis()
    myredis.reconnect()
    kaptcha = myredis.getkaptcha()
    kaptcha = kaptcha[1:-1]
    return kaptcha


if __name__ == '__main__':
    k = get_kaptcha()
    print(k)

