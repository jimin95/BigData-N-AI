from bs4 import BeautifulSoup

fp = open("fruits-vegetables.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

# CSS 선택자로 추출
print(soup.select_one("li:nth-of-type(8)").string) # li태그 8번째 데이터 추출
print(soup.select_one("#ve-list > li:nth-of-type(4)").string) # id값 ve-list의 li태그 4번째 데이터 추출
print(soup.select("#ve-list > li[data-lo='us']")[1].string) # id값 ve-list의 li태그 data-lo속성 index1인 데이터 추출
print(soup.select("#ve-list > li.black")[1].string) # id값 ve-list의 태그li의 class명이 black인 index1 데이터 추출

# find 메서드로 추출
cond = {"data-lo":"us", "class":"black"} # 한번에 조건지정
print(soup.find("li",cond).string)

# find 메서드 연속 사용
print(soup.find(id="ve-list").find("li",cond).string) # 이전에 추출한 요소에 추가적인 조건 지정

#### result ####
# 아보카도
# 아보카도
# 아보카도
# 아보카도
# 아보카도
# 아보카도