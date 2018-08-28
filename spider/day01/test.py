# import requests
# import json
#
# query_string = input('输入')
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
#
# post_data = {
#     "query": query_string,
# }
#
# post_url = "http://fanyi.baidu.com/langdetect"
#
# r = requests.post(post_url, data=post_data, headers=headers)
#
# dict_dict = json.loads(r.content.decode())
# dict = dict_dict['lan']
# if dict == 'zh':
#     post_data = {
#         "query": query_string,
#         "from": "zh",
#         "to": "en",
#     }
# else:
#     post_data = {
#         "query": query_string,
#         "from": "en",
#         "to": "zh",
#     }
# r1 = "http://fanyi.baidu.com/basetrans"
# r = requests.post(r1, data=post_data, headers=headers)
# dict_ret = json.loads(r.content.decode())
# ret = dict_ret["trans"][0]["dst"]
# print("result is :", ret)
p = "abcdef"
t=p[::-1]
print(t)