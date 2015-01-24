import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata=urllib.urlencode({
    '_VIEWSTATE':'dDwyODE2NTM0OTg7Oz4EPWKUJ7QVy9jt5geaO9kcCdS0zQ==',
    'txtUserName':'04123007',
    'TextBox2':'520shazhuzhU',
    'txtSecretCode':'jhn6',
    'RadioButtonList1':'Ñ§Éú',
    'Button1':'',
    'lbLanguage':'',
    'hidPdrs':'',
    'hidsc':''})

req = urllib2.Request(
    url = 'http://222.24.19.201/default2.aspx',
    data = postdata
    )

result = opener.open(req)
print result.read()
