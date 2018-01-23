from bs4 import BeautifulSoup
import urllib.request as req

# wiki : 윤동주
url = "https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = req.urlopen(url)
soup = BeautifulSoup(res,'html.parser')

# Copy Selector : #mw-content-text > div > ul:nth-child(46) > li:nth-child(1)
a_list = soup.select("#mw-content-text > div > ul > li a")

for a in a_list:
    name = a.string
    print("-", name)

#### result ####
# - 하늘과 바람과 별과 시
# - 1976년
# - 별을 사랑하는 아이들아
# - 만주
# - 북간도
# - 만주
# - 지린
# ....