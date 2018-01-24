# urljoin의 특성 : 상대경로 매개변수에 http:// 등으로 시작한다면 기본 URL무시

from urllib.parse import urljoin

base = "http://example.com/html/a.html"

print( urljoin(base,"/hoge.html") )
print( urljoin(base,"http://otherExample.com/wiki") )
print( urljoin(base,"//anotherExample.org/test") )

#### result ####
# http://example.com/hoge.html
# http://otherExample.com/wiki
# http://anotherExample.org/test