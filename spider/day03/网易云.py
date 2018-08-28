from selenium import webdriver
import requests
from lxml import etree
import random
import re
import time
import json


class Wangyimusic:
    def __init__(self):
        self.url = "https://music.163.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
            "Referer": "https://music.163.com/", 'Host': 'music.163.com'}
        self.start = "http://music.163.com/discover/playlist"
        # self.proxies = [{'http': '183.141.124.163:9000'},
        #                 {'http': ' 101.4.136.34:80'},
        #                 {'http': '47.98.234.177:3128'},
        #                 {'http': '183.232.185.61:80'},
        #                 {'http': '58.247.179.94:8060'}]

    def start_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        html_list = html.xpath("//div[@class='bd']/dl")

        for list in html_list:
            title = list.xpath("./dt/text()")[0] if len(list.xpath("./dt/text()")[0]) > 0 else None
            a_href = list.xpath("./dd/a")
            content_list = []
            for a in a_href:
                item = {}
                item["title"] = title
                item["a_list"] = self.url + a.xpath("./@href")[0] if len(a.xpath("./@href")[0]) > 0 else None
                item["a_content"] = a.xpath("./text()")[0] if len(a.xpath("./text()")[0]) > 0 else None
                content_list.append(item)
                # print(content_list)
        return content_list

    def get_list_href(self, href, tot_list):
        content_list = []
        if href["a_list"] is not None:
            # print(href["a_list"])
            html = self.start_url(href["a_list"], )
            html = etree.HTML(html)
            div_list = html.xpath("//ul[@class='m-cvrlst f-cb']/li")

            for div in div_list:
                item = {}
                item['title'] = div.xpath(".//a[@class='msk']/@title")[0] if len(div.xpath(".//a[@class='msk']/@title")[0]) >0 else None
                item['href'] = self.url + div.xpath(".//a[@class='msk']/@href")[0] if len (div.xpath(".//a[@class='msk']/@href")[0]) >0 else None
                item['num'] = div.xpath(".//span[@class='nb']/text()")[0] if len(div.xpath(".//span[@class='nb']/text()")[0]) else None
                item['auther'] = div.xpath(".//a[@class='nm nm-icn f-thide s-fc3']/@title")[0] if len(div.xpath(".//a[@class='nm nm-icn f-thide s-fc3']/@title")[0]) else None
                content_list.append(item)
            tot_list.extend(content_list)
            # print(content_list)
            next_url = self.url + html.xpath("//div[@class='u-page']// a[text() = '下一页'] / @href")[0] if len(html.xpath("//div[@class='u-page']// a[text() = '下一页'] / @href")[0]) else None
            if next_url is not None and next_url != 'https://music.163.comjavascript:void(0)':
                href["a_list"] =  next_url
                return self.get_list_href(href, tot_list)
            print(tot_list)
            return tot_list

    def get_playlist_tracks(self, href):  # 获取每个歌单的歌曲信息
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless")
        driver =webdriver.Chrome(chrome_options=opt)
        driver.get(href['href'])
        driver.switch_to.frame("g_iframe")
        tr_list = driver.find_elements_by_xpath("//tbody/tr")
        playlist_tracks = []
        for tr in tr_list:
            track = {}
            track["name"] = tr.find_element_by_xpath("./td[2]//b").get_attribute("title")
            track["duration"] = tr.find_element_by_xpath("./td[3]/span").text
            track["singer"] = tr.find_element_by_xpath("./td[4]/div").get_attribute("title")
            track["album_name"] = tr.find_element_by_xpath("./td[5]//a").get_attribute("title")
            playlist_tracks.append(track)
        driver.quit()
        return playlist_tracks



    def run(self):
        html_str = self.start_url(self.start)
        href_list = self.get_content_list(html_str)
        for item in href_list:
            tot_list=self.get_list_href(item, [])
            for tot in tot_list:
                singer_list=self.get_playlist_tracks(tot)
                print(singer_list)




if __name__ == '__main__':
    wangyi = Wangyimusic()
    wangyi.run()
