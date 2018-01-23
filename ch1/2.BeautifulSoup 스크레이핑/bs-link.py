# find_all() 매서드를 이용하여 동일태그의 전체 내용 추출

from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

# HTML 분석
soup = BeautifulSoup(html,'html.parser')

# find_all() 매서드로 동일태그의 전체 내용 추출
links = soup.find_all("a")

# 링크 목록 출력
# href 속성은 attrs속성으로, 내부 설명텍스트 string속성으로 추출
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text," > ",href)


#### result ####
# naver  >  http://www.naver.com
# daum  >  http://www.daum.net