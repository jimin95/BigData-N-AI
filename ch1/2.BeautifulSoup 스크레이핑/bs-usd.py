# NAVER 금융 데이터 추출

from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "http://info.finance.naver.com/marketindex"
res = req.urlopen(url)

# HTML 분석
soup = BeautifulSoup(res,'html.parser')

# 원하는 데이터 추출
countries = soup.select("h3.h_lst > span.blind")
prices = soup.select("div.head_info > span.value")

for country in countries:
    print(country.string)

for price in prices:
    print(price.string)

# print("usd/krw = " + usd)

#### result ####
# usd/krw = 1,065.00