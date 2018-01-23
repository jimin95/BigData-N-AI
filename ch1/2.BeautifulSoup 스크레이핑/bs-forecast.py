from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen()으로 데이터 가져오기
res = req.urlopen(url)

# BeautifulSoup으로 분석
soup = BeautifulSoup(res,'html.parser')

# 원하는 데이터 추출
title = soup.find("title").string
wf = soup.find("wf").string

print(title)
print(wf)

#### result ####
# 기상청 육상 중기예보
# 기압골의 영향으로 22일은 제주도에 비가 오겠습니다.<br />그 밖의 날은 고기압의 영향으로 대체로 맑은 날이 많겠습니다
# 겠습니다.<br />강수량은 평년(0~2mm)보다 적겠으나 제주도는 비슷하겠습니다.