import requests
from bs4 import BeautifulSoup
import re
import csv

#url="https://nips.cc/Conferences/2018/Schedule"
#url="https://icml.cc/Conferences/2018/Schedule"
url="https://iclr.cc/Conferences/2018/Schedule"

r=requests.get(url)
html=r.text.encode(r.encoding).decode()
soup=BeautifulSoup(html,'lxml')
info=soup.find_all('div',attrs={'maincardBody'})
list=[li.text for li in info]
print(list)
with open('iclr2018_papers_title.txt','w',encoding='utf8') as f:
    for title in list:
        print(title)
        [f.write('{}\n'.format(title))]


