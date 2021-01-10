#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time
import requests
import Header
from bs4 import BeautifulSoup

__Author__ = 'Sean'


class Login(object):
    """
    登陆类
    """

    def __init__(self):
        self.url = 'http://106.14.133.21:9095/robo/admin/portal/login.jsp'
        self.session = requests.session()
        self.header = Header.Header()

    def get_warning(self):
        j_username = ''
        j_password = ''
        remember = 'on'
        saveflag = '1'

        post_data = "j_username=" + j_username + "&j_password=" + j_password + "&remember" + remember \
                    + "&saveflag=" + saveflag
        headers = self.header.post_login()
        # headers.setdefault("Cookie", str(self.get_cookie(True)))
        # 登陆
        self.session.post(url=self.url, data=post_data, headers=headers, allow_redirects=False)
        # 保存新的cookies
        r = self.session.get(url='http://106.14.133.21:9095/robo/admin/portal/main.jsp',
                             headers=self.header.get_login())
        pc_hash = int(round(time.time() * 1000))
        # --------------------------------
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                ' Chrome/66.0.3359.139 Safari/537.36',
                  'Referer': 'http://106.14.133.21:9095/robo/admin/machine_status/CurrGoodsWay_List.jsp?'
                             'menuid=6102&stamp=0.7493471796448679&pc_hash=%s' % pc_hash}
        pos_data = {
            'param_sell_machine_id': '',
            'param_shop_id': '',
            'param_shop_name': '',
            'param_goods_name': '',
            'param_row_no': '',
            'param_col_no_merge': '',
            'param_machine_name': '长沙',
            'orderbyitem': '5',
            'orderbytype': '0'
        }
        result = self.session.post(url='http://106.14.133.21:9095/robo/admin/machine_status/CurrGoodsWay_List.jsp',
                                   data=pos_data, headers=header, allow_redirects=False)
        soup = BeautifulSoup(result.text, 'lxml')
        tbody = soup.findAll("tbody")
        rows = tbody[1].findAll("tr")
        data = {}
        for row in rows:
            cols = row.findAll("td")
            da = [cols[3].text, cols[4].text, cols[5].text, cols[6].text]
            data.setdefault(cols[2].text, da)
        print(data)


if __name__ == "__main__":
    login = Login()
    login.get_warning()
