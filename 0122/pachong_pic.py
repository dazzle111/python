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

#��ҳ����������
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

#��ҳ������
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
print '��ʼɨ����ҳ...'
host = 'http://desk.zol.com.cn'
indexUrl = '/meinv/'
while(indexUrl != ''):
    print '����ץȡ��ҳ:',host+indexUrl
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
print '��ҳɨ�����,����ͼ�������ѻ��:'
htmlDoorList = indexParser.urlList

class getImagerUrl(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for door in htmlDootList:
            print '��ʼ��ȡͼƬ��ַ����ڵ�ַΪ:',door
            global nextHtmlUrl
            nextHtmlUrl = ''
            while(door != ''):
                print '��ʼ����ҳ%s��ȡͼƬ...' % (host+door)
                if(nextHtmlUrl != ''):
                    request = urllib2.Request(host+nextHtmlUrl)
                else:
                    request = urllib2.Request(host+door)
                try:
                    m = urllib2.urlopen(request)
                    con = m.read()
                    imageParser.feed(con)
                    print '��һ��ҳ���ַΪ:',nextHtmlUrl
                    if(door == nextHtmlUrl):
                        break;
                except urllib2.URLError,e:
                    print e.reason
        print '����ͼƬ��ַ���ѻ��:',imageUrlList

class getImage(threading.Thread):
    def __init__(self):
        global imageUrlList
        print '��ʼ����ͼƬ...'
        while(True):
            print 'Ŀǰ����ͼƬ����:',imageGetCount
            print '������ͼƬ����:',imageDownloadCount
            image = imageUrlList.get()
            print '�����ļ�·��:',image
            try:
                cont = urllib2.urlopen(image).read()
                patter = '[0-9]*\.jpg'
                match = re.search(patter,image)
                if match:
                    print '���������ļ�:',match.group()
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
        print '�ļ�ȫ���������...'

get = getImageUrl()
get.start()
print '��ȡͼƬ�����߳�����:'
time.sleep(2)

download = getImage()
download.start()
print '����ͼƬ�����߳�����:'





















                   
