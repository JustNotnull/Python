# coding=utf-8
import requests
from lxml import etree
import json
import threading
from queue import Queue

class Guoke:
    def __init__(self):
        self.start_url = "https://www.guokr.com/ask/highlight/?page=1"
        self.part_url ="https://www.guokr.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            , }
    def parse_url(self,url):#发送请求，获取响应
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):#提取数据
        html = etree.HTML(html_str)

        div_list = html.xpath("//div[@class='ask-list-detials']") #根据div分组
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./h2//text()")[0] if len(div.xpath("./h2//text()")) > 0 else None
            item["href"] = div.xpath("./h2//@href")[0] if len(div.xpath("./h2//@href")) > 0 else None
            item["content"] = self.get_img_list(item["href"],[])
            item["content"] = item["content"]
            content_list.append(item)
        #提取下一页的url地址
        next_url =self.part_url+ html.xpath("//ul[@class='gpages']/li/a[text()='下一页']/@href")[0] if len(html.xpath("//ul[@class='gpages']/li/a[text()='下一页']/@href"))>0 else None
        return content_list,next_url

    def get_img_list(self,detail_url,total_img_list): #获取帖子中的所有的图片
        #3.2请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        #3.3提取详情页第一页的图片，提取下一页的地址
        img_list = detail_html.xpath("//div[@class='answer-txt answerTxt gbbcode-content']//text()")
        total_img_list.extend(img_list)
        #3.4请求详情页下一页的地址，进入循环3.2-3.4

        return total_img_list

    def save_content_list(self,content_list): #保存数据
        print(content_list)
        with open('gggg.txt',"a",encoding="utf-8") as f:
            for content in content_list:
                print(type(content))
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):#实现主要逻辑
        next_url = self.start_url
        while next_url is not None:
            #1.start_url
            #2.发送请求，获取响应
            html_str = self.parse_url(next_url)
            #3.提取数据，提取下一页的url地址
                #3.1提取列表页的url地址和标题
                #3.2请求列表页的url地址，获取详情页的第一页
                #3.3提取详情页第一页的图片，提取下一页的地址
                #3.4请求详情页下一页的地址，进入循环3.2-3.4
            content_list,next_url = self.get_content_list(html_str)
            #4.保存数据
            self.save_content_list(content_list)
            #5.请求下一页的url地址，进入循环2-5不

if __name__ == '__main__':
    guoke_spider = Guoke()
    guoke_spider.run()
