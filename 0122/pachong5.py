#�ٶ�����
import string,urllib2

def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        sName = string.zfill(i,5)+'.html'
        print '�������ص�'+str(i)+'����ҳ��������洢Ϊ'+sName+'...'
        f= open(sName,'w+')
        m = urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()

bdurl = str(raw_input(u'���������ɵĵ�ַ��ȥ��pn=���������\n'))
begin_page = int(raw_input(u'�����뿪ʼ��ҳ��'))
end_page = int(raw_input(u'�������ص��ҳ��'))

baidu_tieba(bdurl,begin_page,end_page)
