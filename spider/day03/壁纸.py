# coding=utf-8
import requests
from lxml import etree
import random
import time
import re
import json
import threading
from queue import Queue

class Bizhi:
    def __init__(self):
        self.start_url = "http://bizhi.bcoderss.com/page/1/"
        # self.start_url = "http://bizhi.bcoderss.com/"
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
        div_list = html.xpath("//div[@class='wallpaper']") #根据div分组
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./../..//@alt")[0] if len(div.xpath("./../..//@alt")) > 0 else None
            item["href"] = div.xpath("./../..//@href")[0] if len(div.xpath("./../..//@href")) > 0 else None
            content_list.append(item)
            # print(item)
        # 提取下一页的url地址
        next_url =html.xpath("//div[@id='pagination']/a[text()=' 下一页 ']/@href")[0] if len(html.xpath("//div[@id='pagination']/a[text()=' 下一页 ']/@href"))>0 else None
        return  content_list,next_url
    def get_img(self,item):
        html=self.parse_url(item["href"])
        html = etree.HTML(html)
        img_href = html.xpath("//a[@class='download-btn']/@href")[0]

        return img_href

    def save_content_list(self,detail_html_str,file_name_list):
        # print(content_list)
        file_name = file_name_list["title"]
        times=time.time()
        str_name =str(times)[5:10]
        try:
            with open('./pictures/'+file_name+'.jpg', "wb") as f:
                f.write(detail_html_str)
                print("保存成功{}".format(file_name))
        except Exception as e:
            raise e

    def run(self):
        next_url = self.start_url
        while next_url is not  None:
            html_str=self.parse_url(next_url)
            html_href,next_url=self.get_content_list(html_str,)
            print(next_url)
            for img_list in html_href:
                img=self.get_img(img_list)
                pic=self.parse_url(img,)
                self.save_content_list(pic,img_list)



if __name__ == '__main__':
    bizhi_spider = Bizhi()
    bizhi_spider.run()
