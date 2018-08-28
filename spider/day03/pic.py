# coding=utf-8
import requests
from lxml import etree
import random
import time
import os
import re
import json
import threading
from queue import Queue

class Bizhi:
    def __init__(self):
        # self.start_url =
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            , }
        self.proxies = {"http": "http://47.98.234.177:3128",
                        }
    def parse_url(self,url):#发送请求，获取响应
        # print(url)
        response = requests.get(url,headers=self.headers)
        return response.content

    def get_content_list(self,html_str):#提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//tr[@class='tr3 t_one']")[5:-1]
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./td/h3/a/text()")[0] if len(div.xpath("./td/h3/a/text()")) > 0 else None
            item["href"] = "http://d2.sku117.info/pw/"+div.xpath("./td/h3/a/@href")[0] if len(div.xpath("./td/h3/a/@href")) > 0 else None
            content_list.append(item)
            # print(item)
        # 提取下一页的url地址
        # next_url = re.findall("thread.php?fid=14&page=600")
        return  content_list
    def get_img(self,item):
        html=self.parse_url(item["href"])
        html = etree.HTML(html)
        img_href = html.xpath("///div[@class='tpc_content']//img/@src")[0]

        return img_href

    def save_content_list(self,detail_html_str):
        # os.mkdir('./pictures/' + str(file_name_list))
        # print(content_list)
        # file_name = file_name_list["title"]
        times=time.time()
        str_name =str(times)[5:10]

        with open('./pictures/'+str_name+'.jpg', "wb") as f:#'./pictures/' + str(folder) + '/' +
            f.write(detail_html_str)
            # print("保存成功{}".format(file_name))

    def run(self):
        a=5
        next_url = "http://d2.sku117.info/pw/thread.php?fid=14&page={}".format(a)
        while True:
            if a > 600:
                break
            a += 1

            html_str=self.parse_url(next_url)
            html_href=self.get_content_list(html_str,)
            print(next_url)
            for img_list in html_href:
                img=self.get_img(img_list)
                pic=self.parse_url(img)
                print(pic)
                self.save_content_list(pic,)
            next_url = "http://d2.sku117.info/pw/thread.php?fid=14&page={}".format(a)



if __name__ == '__main__':
    bizhi_spider = Bizhi()
    bizhi_spider.run()
