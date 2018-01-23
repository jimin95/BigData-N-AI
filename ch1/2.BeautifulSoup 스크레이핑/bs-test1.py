# 문자열 분석하여 데이터 추출

from bs4 import BeautifulSoup

html = """
<html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 분석 - BeautifulSoup 인스턴스 생성 BeautifulSoup(HTML지정,parser종류지정)
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 요소의 글자 출력
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)


#### result ####
# h1 = 스크레이핑이란?
# p = 웹 페이지를 분석하는 것
# p = 원하는 부분을 추출하는 것