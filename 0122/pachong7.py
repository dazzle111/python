#!/usr/bin/python

import urllib2,HTMLParser,re

host = "http://dex.zol.com.cn"

localSavePath = '/picture/'
startHtmlUrl = ''
htmlUrlList = []
imageUrlList = []

def downloadImage(url):
    cont = urllib2.urlopen(url).read()
    patter = '[0-9]*\.jpg'
    match = re.search(patter,url)
    if match:
        print '���������ļ�:',match.group()
        filename = localSavePath+match.group()
        f = open(filename,'w+')
        f.write(cont)
        f.close()
    else:
        print 'no match'

def getImageUrlByHtmlUrl(htmlUrl):
    parser = MyHtmlParse(False)
    request = urllib2.Request(htmlUrl)
    try:
        response = urllib2.urlopen(request)
        content = response.read()
        parser.feed(content)
    except urllib2.URLError,e:
        print e.reason

class MyHtmlParse(HTMLParser.HTMLParser):
    def __init__(self,isIndex):
        self.isIndex = isIndex
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        if(self.isIndex):
            if(tag == 'a'):
                if(len(attrs) == 4):
                    if(attrs[0] == ('class','pic')):
                        newUrl = host+attrs[1][1]
                        print '�ҵ�һ��ͼƬ����ҳ����:',newUrl
                        global startHtml
                        startHtmlUrl = newUrl
                        getImageUrlByHtmlUrl(newUrl)
        else:
            if(tag == 'img'):
                if(attrs[0] == ('id','bigImg')):
                    imageUrl = attrs[1][1]
                    print '�ҵ�һ��ͼƬ:',imageUrl
                    downloadImage(imageUrl)
            if(tag == 'a'):
                if (len(attrs) == 4):
                    if(attrs[1] == ('class','next')):
                        nextUrl = hhost+attrs[2][1]
                        print '�ҵ�һ��ͼƬ����ҳ����:',nextUrl
                        global startHtmlUrl
                        if(startHtmlUrl != nextUrl):
                            getImageUrlByHtmlUrl(nextUrl)

indexUrl = 'http://desk.zol.com.cn/meinv/'
m = urllib2.urlopen(indexUrl).read()
parserIndex = MyHtmlParse(True)
parserIndex.feed(m)
