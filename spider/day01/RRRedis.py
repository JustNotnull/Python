import  requests
import re
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
            }
url="https://proxy.coderbusy.com/classical/anonymous-type/highanonymous.aspx?page=2"
html = requests.get(url=url,headers=headers)
res=html.text

if res:
  find_ips = re.compile('<td data-ip="(.*?)" data-i=".*?" class="port-box">(.*?)</td>', re.S)
  ip_ports = find_ips.findall(res)
  print(ip_ports)
  for ip in ip_ports:
     a= ip[0].replace("'",'').strip()
     b= ip[1].replace("'",'').strip()
     c= a + ':' + b
     print(c)

  # for address_port in ip_ports:
  #   yield address_port
