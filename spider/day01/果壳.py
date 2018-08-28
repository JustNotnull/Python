import requests
import json
from lxml import etree


class Douban():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            , }

        self.url = "https://www.guokr.com/ask/highlight/?page={}"

    def send_url(self,i):  # 发送请求,获取相应
        response = requests.get(url=self.url.format(i), headers=self.headers)
        print("第{}页".format(i))
        return response.content.decode()

    def get_content(self, send_content,i):  # 接受数据,处理数据
        url_content =etree.HTML(send_content)
        url_href=url_content.xpath("//div[@class='ask-list-detials']//h2//@href")
        url_text=url_content.xpath("//div[@class='ask-list-detials']//h2//text()")
        print(url_href)
        print(url_text)
        # for href in url_href:
        #     item = {}
        #     item["href"] = href
        #     item["title"] = url_text[url_href.index(href)]
        #     print(item)
        # print("*"*500)
        ret3 =url_content.xpath("//div[@class='ask-list-detials']")
        with open('guoke.txt', 'a', encoding='utf-8') as f:
            f.write('第{}页'.format(i))
            f.write('\n')

            for i in ret3:
                item = {}
                item["href"] = i.xpath("./h2//@href")[0] if len(i.xpath("./h2//@href")) > 0 else None
                item["title"] = i.xpath("./h2//text()")[0] if len(i.xpath("./h2//text()")) > 0 else None
                f.write(json.dumps(item,ensure_ascii=False))
                f.write('\n')



        # return json.dumps(list, ensure_ascii=False)



    def save_content(self, send_content):  # 保存数据
        with open('guoke.txt', 'w', encoding='utf-8') as f:
            f.write(send_content)



    def run(self):  # 运行
        i = 0
        while True:
            i += 1
            try:
                send_content = self.send_url(i)
                send_content=self.get_content(send_content,i)
            except:
                break

            print('爬取成功')

        # self.save_content(send_content)


if __name__ == '__main__':
    douban = Douban()
    douban.run()
