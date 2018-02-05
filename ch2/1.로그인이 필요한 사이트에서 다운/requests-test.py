# requests 모듈을 이용해서 get 하여 데이터 추출
# requests에는 get,post,put,delete,head 가능 
import requests

# GET 요청
r = requests.get("http://api.aoikujira.com/time/get.php")
# CF) POST 요청
# req = requests.post("http://~~",data={"key":value,})

# 텍스트 형식으로 데이터 추출
text = r.text
print(text)

# 바이너리 형식으로 데이터 추출
bin = r.content
print(bin)

#### result ####
# 2018/02/05 19:55:49
# b'2018/02/05 19:55:49' -> 파이썬에서 b'~~' 는 바이너리라는 것을 의미