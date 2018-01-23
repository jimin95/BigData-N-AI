# 실습4 : HTML의 문서 텍스트 읽어오기 + URL에 변수 지정하여

import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# (딕셔너리-dict 자료형 변수)매개변수를 URL 인코딩
values = {
    'stnId': '108'
}

params = urllib.parse.urlencode(values)

#요청 전용 URL 생성
url = API + "?" + params
print("url = ", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

#### 결과 ####
# ...
#                                 <data>
#                                         <mode>A01</mode>
#                                         <tmEf>2018-01-19 00:00</tmEf>
#                                         <wf>구름많음</wf>
#                                         <tmn>6</tmn>
#                                         <tmx>10</tmx>
#                                         <reliability>보통</reliability>
#                                 </data>


#                                 <data>
#                                         <mode>A01</mode>
#                                         <tmEf>2018-01-20 00:00</tmEf>
#                                         <wf>구름많음</wf>
#                                         <tmn>5</tmn>
#                                         <tmx>10</tmx>
#                                         <reliability>보통</reliability>
#                                 </data>


#                                 <data>
#                                         <mode>A01</mode>
#                                         <tmEf>2018-01-21 00:00</tmEf>
#                                         <wf>구름많음</wf>
#                                         <tmn>4</tmn>
#                                         <tmx>11</tmx>
#                                         <reliability>보통</reliability>
#                                 </data>


#                 </location>




#         </body>
# </description>
# </item>
# </channel>
# </rss>