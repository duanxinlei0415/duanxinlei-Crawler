# coding:utf-8
import bs4
from bs4 import BeautifulSoup

with open('E:/advancedCrawler/week1/the_blah.html','r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    #print Soup
    #images = Soup.select('body > div.main-content > ul > li:nth-of-type(1) > img')
    images = Soup.select('body > div.main-content > ul > li > img')
    titles = Soup.select('body > div.main-content > ul > li > h3 > a')
    descs = Soup.select('div.main-content > ul > li > p')
    #print(images,titles,descs)


for title in titles:
    print(title.get_text())

for title,image,desc in zip(titles,images,descs):
    data = {
        'title':title.get_text(),
        'image':image.get('src'),
        'desc':desc.get_text()
    }
    print(data)

#body > div.main-content > ul > li:nth-child(1) > img
#body > div.main-content > ul > li:nth-child(1) > h3 > a
#body > div.main-content > ul > li:nth-child(1) > p
