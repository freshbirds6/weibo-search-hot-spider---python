import requests
import re
from bs4 import BeautifulSoup
def spider():
    web=requests.get('https://s.weibo.com/top/summary')
    soup=BeautifulSoup(web.text)
    soup=soup.find_all('a')
    soup=str(soup)

    titl='<a href=".*?">(.*?)</a>'
    title=re.findall(titl,soup,re.S)
    del title[-9:]
    del title[:2]
    i=0
    for titles in title:
        print(str(i) + titles)
        i+=1

spider()
