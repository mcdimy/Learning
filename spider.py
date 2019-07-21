
from urllib import request

class Spider():
    url = 'http://www.le.com/ptv/vplay/27444833.html' 

    def __fetch_content(self):
        r  = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        a = 1
    def __analysis(self,htmls):
        pass

    def go(self):
        self.__fetch_content()
        self.__analysis(htmls)

spider = Spider()
spider.go()


# kasdkjashdkjashdka 

