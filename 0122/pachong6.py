#抓糗百内容
import urllib2
import urllib
import re
import thread
import time

class Spider_Model:

        def __init__(self):
            self.page = 1
            self.pages = []
            self.enable = False

        def GetPage(self,page):
            myUrl = 'http://m.qiushibaike.com/hot/page/'+page
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent' : user_agent}
            req = urllib2.Request(myUrl, headers = headers)
            myResponse = urllib2.urlopen(req)
            myPage = myResponse.read()

            unicodePage = myPage.decode("utf-8")

            myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
            items = []
            for item in myItems:
                items.append([item[0].replace("\n",""),item[1].replace("\n","")])
            return items

        def LoadPage(self):
            while self.enable:
                if len(self.pages) < 2:
                    try:
                        myPage = self.GetPage(str(self.page))
                        self.page += 1
                        self.pages.append(myPage)
                    except:
                        print '无法连接糗事百科'
                else:
                    time.sleep(1)

        def ShowPage(self,nowPage,page):
            for items in nowPage:
                print '第%d页' % self.page,items[0],items[1]
                myInput = raw_input()
                if myInput == "quit":
                    self.enable = False
                    break

        def Start(self):
            self.enable = True
            page = self.page

            print '正在加载中请稍候...'

            thread.start_new_thread(self.LoadPage,())

            while self.enable:
                if self.pages:
                    nowPage = self.pages[0]
                    del self.pages[0]
                    self.ShowPage(nowPage,page)
                    page += 1


print "''"

print '请按下回车浏览今日的糗百内容:'
raw_input(' ')
myModel = Spider_Model()
myModel.Start()
