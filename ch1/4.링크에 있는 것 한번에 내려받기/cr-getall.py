# 중요!!
# 파이썬 매뉴얼을 재귀적으로 다운받는 프로그램

from bs4 import BeautifulSoup
from urllib.parse import *   # URL분석
from urllib.request import * # 인터넷에서 데이터를 내려받기 위함
from os import makedirs      # 폴더 생성을 위함
import os.path,time,re       # os.path:경로 관련, time:슬립(잠시 쉼) 관련, re:정규식 표현

# 이미 처리한 파일인지 확인하기 위한 변수 - 전역변수 초기화
proc_files = {}

# HTML 내부에 있는 링크를 추출하는 함수
def enum_links(html,base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']") # CSS
    links += soup.select("a[href]") # 링크
    result = []
    
    # href 속성 추출, 링크 절대 경로로 변환
    for a in links:
        href = a.attrs['href']
        url = urljoin(base,href)
        result.append(url)
    
    return result

# 파일을 다운받고 저장하는 함수
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    
    if re.search(r"/$",savepath): # 폴더라면 index.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    
    # 모두 다운됐는지 확인
    if os.path.exists(savepath): return savepath
    
    # 다운받을 폴더 생성
    if not os.path.exists(savedir):
        print("mkdir=",savedir)
        makedirs(savedir)
    
    # 파일 다운받기
    try:
        print("download=",url)
        urlretrieve(url,savepath) # 파일 다운로드
        time.sleep(1) # 1초 휴식(처리 중단) - 웹 서버에 부하를 주지 않기 위함
        return savepath
    except:
        print("다운 실패: ",url)
        return None

# HTML 분석하고 다운받는 함수
def analyze_html(url,root_url):
    savepath = download_file(url)

    if savepath is None: return
    if savepath in proc_files: return # 이미 처리됐다면 실행하지 않음
    
    proc_files[savepath] = True
    print("analyze_html=",url)

    # 링크 추출
    html = open(savepath,"r",encoding="utf-8").read()
    links = enum_links(html,url)

    for link_url in links:
        #링크가 루트 이외의 경로를 나타낸다면 무시
        if link_url.find(root_url) != 0:
            if not re.search(r".css$",link_url): continue
        
        # HTML 이라면
        if re.search(r".(html|htm)$",link_url):
            # 재귀적으로 HTML파일 분석
            analyze_html(link_url,root_url)
            continue
        
        # 기타 파일
        download_file(link_url)

# __name__: 모듈이름만 들어옴. 모듈이 아닌경우 "__main__"이 들어옴
if __name__ == "__main__":
    # url에 있는 모든 것 다운
    url = "https://docs.python.org/3.5/library"
    analyze_html(url,url)

#### result ####
# mkdir= ./docs.python.org/3.5
# download= https://docs.python.org/3.5/library
# analyze_html= https://docs.python.org/3.5/library
# mkdir= ./docs.python.org/_static
# download= https://docs.python.org/_static/pydoctheme.css
# download= https://docs.python.org/_static/pygments.css