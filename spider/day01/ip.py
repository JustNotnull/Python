import requests
import json
import  re
import time
from lxml import etree


class Douban():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            , }

        self.url = "https://proxy.coderbusy.com/classical/https-ready.aspx?page={}"
        self.proxies = {"http":"http://114.228.74.196:6666"}

    def send_url(self,i):  # 发送请求,获取相应
        response = requests.get(url=self.url.format(i), headers=self.headers,proxies=self.proxies)

        print("第{}页".format(i))
        ret = response.content.decode()
        # print(ret)
        return ret

    def get_content(self, send_content,i):  # 接受数据,处理数据
        result=re.findall(r'<td data-ip="(.*?)" data-i=".*?" class="port-box">(.*?)</td>',send_content)
        print(result)
        with open('ip.txt', 'a', encoding='utf-8') as f:
            f.write('第{}页'.format(i))
            f.write('\n')
            for i in result:
                f.write(json.dumps(i,ensure_ascii=False))
                f.write('\n')







    # def save_content(self, send_content):  # 保存数据
    #     with open('guoke.txt', 'w', encoding='utf-8') as f:
    #         f.write(send_content)



    def run(self):  # 运行
        i = 1061
        while True:
            time.sleep(2)
            i += 1
            try:
                send_content = self.send_url(i)
                self.get_content(send_content,i)
            except:

                break

            print('爬取成功')

        # self.save_content(send_content)


if __name__ == '__main__':
    douban = Douban()
    douban.run()
