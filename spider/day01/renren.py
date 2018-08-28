import  requests

session=requests.session()
url='http://www.renren.com/PLogin.do'
data={'email':'mr_mao_hacker@163.com','password':'alarmchime'}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
# cookie = {'Cookie': 'anonymid=jiefsaewmcphj1; depovince=GW; jebecookies=830ab8b2-9c71-45f6-9bb4-25dd4106f420|||||; _r01_=1; ick_login=d2b2a9a9-1e56-4f3b-ad04-566b46ffdc55; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=a69cb656dc6a0ddef2ee8450b425f0d19; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20180614/1515/main_yJK9_18cb000005581986.jpg; t=8474bf12c1f0c8b23280152228288a859; societyguester=8474bf12c1f0c8b23280152228288a859; id=327550029; loginfrom=syshome; ch_id=10016; JSESSIONID=abcgoo9ZMRucLdso899pw; jebe_key=041fe690-addf-4998-bb1f-bc2a05e1a965%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1528974266370%7C1%7C1528974269765; wp_fold=0; xnsid=1fb9e54'}
response=session.post(url,headers=headers,data=data)
with open('ren.txt','w',encoding='utf-8') as f:
    f.write(response.content.decode())