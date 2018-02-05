# 로그인한 상태에서만 가져올 수 있는 정보 수집
# session을 이용

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디와 비밀번호
user_id = "<본인의 id>"
password = "<본인의 password>"

# session 시작
session = requests.session()

login_info = {
   "m_id": user_id,
   "m_passwd": password
}

# login
url_login = "http://www.hanbit.co.kr/member/login_proc.php" # headers 정보에서 가져옴
res = session.post(url_login,data=login_info)
res.raise_for_status() # 오류 발생시 예외 발생

# 마이페이지 접근
url_mypage = "http://www.hanbit.co.kr/member/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text,"html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_session2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)