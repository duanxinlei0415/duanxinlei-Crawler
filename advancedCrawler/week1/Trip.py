import bs4,requests
from bs4 import BeautifulSoup

url = 'http://www.tripadvisor.cn/Hotels-g60763-New_York_City_New_York-Hotels.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#print(soup)
titles = soup.select('div.listing_title a ')
imgs = soup.select('img[height="200"]')
cates = soup.select('div.clickable_tags')
#print(titles)
#print(imgs)
#print(cates)
for title,img,cate in zip(titles,imgs,cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings)
    }

print(data)

