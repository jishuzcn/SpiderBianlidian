#!/usr/bin/python
# -*- coding:utf-8 -*-


class Header(object):
    """
    完全模拟浏览器请求头、不带Cookie
    """

    def __init__(self):
        pass

    @staticmethod
    def get_login():
        """
        GET http://106.14.133.21:9095/robo/admin/portal/login.jsp HTTP/1.1
        :return: list
        """
        header = {
            'Host': '106.14.133.21:9095',
            'Proxy-Connection': 'keep-alive',
            'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }
        return header

    @staticmethod
    def post_login():
        """
        POST http://106.14.133.21:9095/robo/admin/portal/login.jsp HTTP/1.1
        :return:list
        """
        header = {
            'Host':'106.14.133.21:9095',
            'Proxy-Connection':'keep-alive',
            'Content-Length':'55',
            'Cache-Control':'max-age=0',
            'Origin':'http://106.14.133.21:9095',
            'Upgrade-Insecure-Requests':'1',
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/66.0.3359.139 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer':'http://106.14.133.21:9095/robo/admin/portal/login.jsp',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
        }
        return header
