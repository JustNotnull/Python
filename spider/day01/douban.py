import requests
from retrying import retry
import json


@retry(stop_max_attempt_number=3)
def douban(count):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
        "Referer": "https://m.douban.com/tv/american"}


    url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1529481198406".format(count)

    response =requests.get(url=url,headers=headers,)
    r=response.content.decode()
    r1=json.loads(r)
    with open('douban.json','a',encoding='utf-8') as f:
        json.dump(r1,f,ensure_ascii=False,indent=1)
    print(type(r1))
for count in range(1,5):
    count*=18
    douban(count)

