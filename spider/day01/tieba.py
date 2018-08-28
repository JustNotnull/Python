import requests


class Tieba():
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = "https://tieba.baidu.com/f?kw=" + tieba_name + "=ala0&tpl={}"
        self.headers = {
            }
        self.proxies = {"http":"http://163.177.151.23:80"}
    def get_url(self):
        return [self.url.format(i * 50) for i in range(2)]

    def get_content(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_content(self, html_str, page_num):
        find_data = '{}第{}页.txt'.format(self.tieba_name, page_num)
        with open(find_data, 'w', encoding='utf8') as f:
            f.write(html_str)

    def run(self):
        url_list = self.get_url()
        for url in url_list:
            html_str = self.get_content(url)
            page_num = url_list.index(url) + 1
            self.save_content(html_str, page_num)


if __name__ == '__main__':
    tb = Tieba('李毅')
    tb.run()
