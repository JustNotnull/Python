from selenium import webdriver
import time
import json

class Douyu:
    def __init__(self):
        self.start_url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def get_url(self):
        room_list=self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        content_list=[]
        for i in room_list:
            item ={}
            item['room_img'] = i.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            item['title_name'] =i.find_element_by_xpath(".//h3[@class='ellipsis']").text
            item['class_name'] =i.find_element_by_xpath(".//div/span[@class='tag ellipsis']").text
            item['actor_name'] =i.find_element_by_xpath(".//div/p/span[@class='dy-name ellipsis fl']").text
            item['online_number'] =i.find_element_by_xpath(".//div/p/span[@class='dy-num fr']").text
            content_list.append(item)
            print(item)
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url)>0 else None
        print(next_url)
        return content_list,next_url
    def save_content(self,content_list):
        with open('douyu.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(content_list,ensure_ascii=False))
            f.write('\n')
        # print(content_list)
    def run(self):
        # 1设置初始地址,发起请求,获取response

        self.driver.get(self.start_url)
        # 2处理数据
        content_list,next_url=self.get_url()
        # 3保存数据
        self.save_content(content_list)
        # 4获取下一页
        while next_url is not None:
            next_url.click()
            time.sleep(5)
            content_list, next_url = self.get_url()
            # 3保存数据
            self.save_content(content_list)

if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
