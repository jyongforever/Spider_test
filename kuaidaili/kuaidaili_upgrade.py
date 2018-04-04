#! /usr/bin/env python
# -*- coding:utf-8 -*-
import random
import requests
import lxml.html
from selenium import webdriver
import time

class Kuaidaili():
    def __init__(self,page):
        # 构造url
        self.urls = ['https://www.kuaidaili.com/free/inha/{}'.format(i) for i in range(1,page+1)]  # 高匿代理

        # 构造请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
        # 每次爬取ip，清空原ip文件
        with open('ip.txt','w') as f:
            f.write('')
        # 创建一个文件用来存储ip
        self.file = open('ip.txt','a')
        self.driver = webdriver.Chrome()
        # self.flag = False
    def parse_url(self,url):
        # if not self.flag:
        #     time.sleep(3)
        #     self.flag = True
        time.sleep(3)
        self.driver.get(url)
        html_str = self.driver.page_source
        tree = lxml.html.fromstring(html_str)
        return tree

    def save_data(self,data):
        self.file.write(data+'\n')

    def __del__(self):
        self.driver.close()
        self.file.close()

    def run(self):

        for n,url in enumerate(self.urls):
            tree = self.parse_url(url)
            tr_str = '//*[@id="list"]/table/tbody/tr'
            tr_list = tree.xpath(tr_str)
            for tr in tr_list:
                ip_str = './td[1]/text()'
                port_str = './td[2]/text()'
                response_str = './td[6]/text()'
                ip = tr.xpath(ip_str)[0]
                port = tr.xpath(port_str)[0]
                rs = tr.xpath(response_str)[0]
                data = ip+':'+port
                print(str(n+1)+'|'+data)
                self.save_data(data)

if __name__ == '__main__':
    kuaidaili = Kuaidaili(100)
    kuaidaili.run()








