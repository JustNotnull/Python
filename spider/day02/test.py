# import  requests
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
#            "Referer":"https://music.163.com/",'Host': 'music.163.com'}
# url = "https://music.163.com/discover/playlist/?cat=华语"
# response = requests.get(url=url,headers=headers)
# ret= response.content.decode()
# print(ret)

import  time
times =time.time()

print(times)
str=str(times)[5:10]
print("yyyy"+str)