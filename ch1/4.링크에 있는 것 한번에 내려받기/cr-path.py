# 상대경로 -> 절대경로로 변환하여 다운로드해야함

# urllib.parse.urljoin() : 상대경로를 전개할 때 사용 (절대경로로 뽑아냄)
# urljoin(기본URL, 상대경로)
from urllib.parse import urljoin

base = "http://example.com/html/a.html"  # 파일 다운로드 링크

print( urljoin(base,"b.html") )
print( urljoin(base,"sub/c.html") )
print( urljoin(base,"../index.html") )
print( urljoin(base,"../img/hoge.png") )
print( urljoin(base,"../css/hoge.css") )

#### result ####
# http://example.com/html/b.html
# http://example.com/html/sub/c.html
# http://example.com/index.html
# http://example.com/img/hoge.png
# http://example.com/css/hoge.css