# requests 모듈을 이용하여 이미지 데이터 추출

import requests

r = requests.get("http://wikibook.co.kr/wikibook.png")

# 바이너리 형식으로 데이터 저장 - 리턴값의 text나 content 속성을 참조하면 내부 터이터 확인 가능
with open("test.png","wb") as f:
    f.write(r.content)

print("saved!")

#### results ####
# saved!
# test.png 파일 다운로드 되어있음