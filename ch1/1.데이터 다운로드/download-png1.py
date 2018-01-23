# 실습1 : 이미지 읽어와 바로 저장

# urllib 라이브러리 읽어들이기
import urllib.request

# URL과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
urllib.request.urlretrieve(url, savename)
print("저장되었습니다.")