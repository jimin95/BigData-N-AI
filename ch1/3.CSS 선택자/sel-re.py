from bs4 import BeautifulSoup
import re # 정규식 표현 사용 시

html = """
<ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://example.com/fuga">fuga*</li>
    <li><a href="https://example.com/foo">foo*</li>
    <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""

soup = BeautifulSoup(html,"html.parser")

# 정규식으로 href에서 https인 것 추출
li = soup.find_all(href=re.compile(r"^https://")) # compile()함수로 정규표현식 생성
for e in li:
    print(e.attrs['href'])

#### result ####
# https://example.com/fuga
# https://example.com/foo