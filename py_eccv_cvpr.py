import requests
from bs4 import BeautifulSoup
import re
import csv

url="http://openaccess.thecvf.com/ECCV2018.py"
r=requests.get(url)
html=r.text.encode(r.encoding).decode()
soup=BeautifulSoup(html,'lxml')
info=soup.find_all('dt')
list=[li.find('a').text for li in info]

with open('eccv2018_papers_title.txt','w',encoding='utf8') as f:
    for title in list:
        print(title)
        [f.write('{}\n'.format(title))]


