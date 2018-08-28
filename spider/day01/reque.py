import  requests

response = requests.get("http://www.sina.com.cn/")
# response.encoding='utf-8'
# response=response.text
response=response.content
with open('a.txt','wb') as f:
    f.write(response)
print(response)
