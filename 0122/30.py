import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata=urllib.urlencode({
    'username':'¡Œ…˘‹∞',
    'password':'karongxing'
  })

req = urllib2.Request(
    url = 'http://cs.xiyoulinux.org/',
    data = postdata
    )

result = opener.open(req)
print result.read()
