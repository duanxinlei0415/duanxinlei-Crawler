# coding:utf8
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
    #这里的init初始化是两个下划线，不是一个下划线
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        #下面用add_new_url而不是add_new_urls，因为root_url是一个，不是一组！！
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count = count + 1
            except Exception as e:
                print('craw failed', e)


        self.outputer.output_html()

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
   # print 'url=',root_url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)