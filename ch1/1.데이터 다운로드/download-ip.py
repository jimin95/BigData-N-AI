# 실습3 : HTML의 문서 텍스트 읽어오기

# IP 확인 API로 접근해서 결과 출력하기 - 클리아언트 접속 정보 출력
import urllib.request

# 데이터 읽어들이기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리를 문자열로 반환
text = data.decode("utf-8")
print(text)


#### 결과 ####
# [ip]
# API_URI=http://api.aoikujira.com/ip/get.php
# REMOTE_ADDR=121.133.245.125
# REMOTE_HOST=121.133.245.125
# REMOTE_PORT=59216
# HTTP_HOST=api.aoikujira.com
# HTTP_USER_AGENT=Python-urllib/3.6
# HTTP_ACCEPT_LANGUAGE=
# HTTP_ACCEPT_CHARSET=
# SERVER_PORT=80
# FORMAT=ini