# 실습2 : 이미지 읽어와 변수에 저장한 후 파일 저장

import urllib.request

# URL과 저장 경로 지정
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

# 다운로드 - 이미지를 읽어와 변수에 저장
memory = urllib.request.urlopen(url).read()

# 파일 저장 
# open( ,mode="읽기r/쓰기b-바이너리")
with open(savename, mode="wb") as f:
    f.write(memory)
    print("이미지 저장에 성공하였습니다.")