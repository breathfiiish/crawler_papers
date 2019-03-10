import json
import csv
import pandas as pd
with open('links-between-papers-and-code.json','r') as load_f:
    load_dict = json.load(load_f)

with open('iclr2018.csv', 'w') as f:
    [f.write('{},{},{}\n'.format('paper_title','papers_link','code_link'))]

papers_list=[]
with open('iclr2018_papers_title.txt','r',encoding='utf8') as pf:
    for line in pf:
        line=line.replace('\n','')
        papers_list.append(line)

for paper in papers_list:
    title=paper
    title=title.replace(',','\\,')
    code_link=0
    for i in range(len(load_dict)):
        if load_dict[i]['paper_title']==title:
            code_link+=1
            with open('iclr2018.csv','a',encoding='utf8') as f:
                if code_link <=1 :
                    print('{},{},{}\n'.format(load_dict[i]['paper_title'],load_dict[i]['paper_url_abs'],load_dict[i]['repo_url']))
                    [f.write('{},{},{}\n'.format(title,load_dict[i]['paper_url_abs'],load_dict[i]['repo_url']))]
                else:
                    [f.write('{},{},{}\n'.format('','',load_dict[i]['repo_url']))]


