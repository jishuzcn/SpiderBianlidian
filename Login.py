#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
import Header
import os

__Author__ = '汪思源'


def save_cookie(cookie):
    f = open(r"/FuleiBLD.txt", "w")
    f.write(cookie)
    f.close()


class Login(object):
    """
    登陆类
    """

    def __init__(self):
        self.url = 'http://106.14.133.21:9095/robo/admin/portal/login.jsp'
        self.session = requests.session()
        self.header = Header.Header()

    def doLogin(self):
        j_username = 'bjfl'
        j_password = '88888'
        remember = 'on'
        saveflag = '1'

        post_data = "j_username=" + j_username + "&j_password=" + j_password + "&remember" + remember + "&saveflag=" + saveflag
        headers = self.header.post_login()
        headers.setdefault("Cookie",self.get_cookie())
        print(headers)
        result = self.session.post(url=self.url, data=post_data, headers=headers)
        # 保存新的cookies
        print(result.cookies)


    def isLogin(self):
        pass

    def get_cookie(self, flag=False):
        if not os.path.exists(r"/FuleiBLD.txt") or flag:
            r = self.session.get(url=self.url, headers=self.header.get_login())
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            save_cookie(str(cookies))
        else:
            try:
                f = open(r"/FuleiBLD.txt", "r")
                cookies = f.read()
            finally:
                pass
        return cookies


if __name__ == "__main__":
    login = Login()
    login.doLogin()
