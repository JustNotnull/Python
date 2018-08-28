import requests
import json


class Fanyi():
    def __init__(self, query_string):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

        self.post_data = {
            "query": query_string,
        }

        self.post_url = "http://fanyi.baidu.com/langdetect"

        self.r1 = "http://fanyi.baidu.com/basetrans"

    def get_url(self):
        return requests.post(self.post_url, data=self.post_data, headers=self.headers)

    def get_content(self, url):
        dict_dict = json.loads(url.content.decode())
        return dict_dict['lan']

    def show_content(self, content):
        if content == 'zh':
            self.post_data = {
                "query": query_string,
                "from": "zh",
                "to": "en",
            }
        else:
            self.post_data = {
                "query": query_string,
                "from": "en",
                "to": "zh",
            }
        r = requests.post(self.r1, data=self.post_data, headers=self.headers)
        dict_ret = json.loads(r.content.decode())
        ret = dict_ret["trans"][0]["dst"]
        print("result is :", ret)

    def run(self):
        url = self.get_url()
        content = self.get_content(url)
        self.show_content(content)


if __name__ == '__main__':
    query_string = input('输入')
    fanyi = Fanyi(query_string)
    fanyi.run()
