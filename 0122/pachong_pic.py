#!/usr/bin/python 

import re,urllib2,HTMLParser,threading,Queue,time

htmlDoorList = []
htmlUrlList = []
imageUrlList = Queue.Queue(0)
imageGetCount = 0
imageDownloadCount = 0
nextHtmlUrl = ''
localSavePath = '/data/1920*1080/'

replace_str = '1920*1080'
replaced_str = '960*600'

#内页分析处理类
class ImageHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.nextUrl = ''
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attrs):
        global imageUrlList
        if(tag == 'img' and len(attrs) > 2):
            if(attrs[0] == ('id','bigImg')):
                url = attrs[1][1]
                url = url.replace(replaced_str,replace_str)
                imageUrlList.put(url)
                global imageGetCount
                imageGetCount = imageGetCount + 1
                print url
        elif(tag == 'a' and len(attrs) == 4) :
            if(attrs[0] == ('id','pageNext') and attrs[1]==('class','next')):
                global nextHtmlUrl
                nextHtmlUrl = attrs[2][1]

#首页分析类
class IndexHtmlParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.urlList = []
        self.index = 0
        self.nextUrl = ''
        self.tagList = ['li','a']
        self.classList = ['photo-list-padding','pic']
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self,tag,attr):
        if(tag == self.tagList[self.index]):
            for attr in attrs:
                if(attr[1] == self.classList[self.index]):
                    if(self.index == 0):
                        self.index = 1
                    else:
                        self.index = 0
                        print attrs[1][1]
                        self.urlList.append(attrs[1][1])
                        break
        elif(tag == 'a'):
            for attr in attrs:
                if(attr[0] == 'id' and attr[1] =='pageNext'):
                    self.nextUrl = attrs[1][1]
                    print 'nextUrl:',self.nextUrl
                    break

indexParser = IndexHtmlParser()
imageParser = ImageHtmlParser()
print '开始扫面首页...'
host = 'http://desk.zol.com.cn'
indexUrl = '/meinv/'
while(indexUrl != ''):
    print '正在抓取网页:',host+indexUrl
    request = urllib2.Request(host+indexUrl)
    try:
        m = urllib2.urlopen(request)
        con = m.read()
        indexParser.feed(con)
        if(indexUrl == indexParser.nextUrl):
            break
        else:
            indexUrl = indexParser.nextUrl
    except urllib2.URLError,e:
        print e.reason
print '首页扫描完成,所有图集链接已获得:'
htmlDoorList = indexParser.urlList

class getImagerUrl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for door in htmlDootList:
            print '开始获取图片地址，入口地址为:',door
            global nextHtmlUrl
            nextHtmlUrl = ''
            while(door != ''):
                print '开始从网页%s获取图片...' % (host+door)
                if(nextHtmlUrl != ''):
                    request = urllib2.Request(host+nextHtmlUrl)
                else:
                    request = urllib2.Request(host+door)
                try:
                    m = urllib2.urlopen(request)
                    con = m.read()
                    imageParser.feed(con)
                    print '下一个页面地址为:',nextHtmlUrl
                    if(door == nextHtmlUrl):
                        break;
                except urllib2.URLError,e:
                    print e.reason
        print '所有图片地址均已获得:',imageUrlList

class getImage(threading.Thread):
    def __init__(self):
        global imageUrlList
        print '开始下载图片...'
        while(True):
            print '目前捕获图片数量:',imageGetCount
            print '已下载图片数量:',imageDownloadCount
            image = imageUrlList.get()
            print '下载文件路径:',image
            try:
                cont = urllib2.urlopen(image).read()
                patter = '[0-9]*\.jpg'
                match = re.search(patter,image)
                if match:
                    print '正在下载文件:',match.group()
                    filename = localSavePath+match.group()
                    f = open(filename,'wb')
                    f.write(cont)
                    f.close()
                    global imageDownloadCount
                    imageDownloadCount = imageDownloadCount + 1
                else:
                    print 'no match'
                if(imageUrlList.empty()):
                    break;
            except urllib2.URLError,e:
                print e.reason
        print '文件全部下载完成...'

get = getImageUrl()
get.start()
print '获取图片链接线程启动:'
time.sleep(2)

download = getImage()
download.start()
print '下载图片链接线程启动:'





















                   
