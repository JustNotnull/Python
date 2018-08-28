import requests
import json

class Douban():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
            "Referer": "https://m.douban.com/tv/american"}

        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1529481198406"

    def send_url(self):#发送请求,获取相应
        response = requests.post(url=self.url,headers=self.headers)
        return response.content.decode()
    def get_content(self,send_dict):#接受数据,处理数据
        dict_ret=json.loads(send_dict)
        json_ret =dict_ret["subject_collection_items"]
        return json_ret
    def save_content(self,content):#保存数据
        with open('douban.txt', 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=1)
    def run(self):#运行
        send_dict=self.send_url()
        html=self.get_content(send_dict)
        content=self.save_content(html)

if __name__ == '__main__':
    douban = Douban()
    douban.run()