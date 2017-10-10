import requests
from bs4 import BeautifulSoup

#
# function spider_by_get():
#     newsUrl = "http://news.sina.com.cn/china/"
#     res = requests.get(newsUrl)
#     res.encoding = "utf-8"
#     print(res.text)
#
# if (__name__ == "__main_"):
#     spider_by_get()


newsUrl = "http://news.sina.com.cn/china/"
res = requests.get(newsUrl)
res.encoding = 'utf-8'
# print(res.text)
parseContent = res.text

soup = BeautifulSoup(parseContent, "html.parser")
print(soup.text)



