import  requests
from lxml import etree
import  json
url = "https://api.bilibili.com/x/v1/dm/list.so?oid=42859864"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    }

response = requests.get(url=url,headers=headers)
html=etree.HTML(response.content)
html_str=html.xpath("//i/d//text()")
for i in  html_str:
    with open('./danmu/bili.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(i,ensure_ascii=False))
        f.write('\n')
print(html_str)