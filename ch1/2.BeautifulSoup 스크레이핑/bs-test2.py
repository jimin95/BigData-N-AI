# find() 매서드를 이용해 id 속성을 지정하여 데이터 추출

from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p id="body">원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석
soup = BeautifulSoup(html,'html.parser')

# find() 매서드로 원하는 부분 추출
title = soup.find(id="title")
body = soup.find(id="body")

# 텍스트 부분 출력
print(" #title = " + title.string)
print(" #body = " + body.string)


#### result ####
 #title = 스크레이핑이란?
 #body = 원하는 부분을 추출하는 것
