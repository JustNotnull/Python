import  requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
url ="http://36kr.com/"

response = requests.get(url=url,headers=headers)
r = response.content.decode()


print(r)