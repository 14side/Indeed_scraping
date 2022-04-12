from ast import Lambda
from cgitb import text
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_link = 'https://www.indeed.com'


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.27'}

df = pd.DataFrame(columns = ['Title','Link'])

for number in range(0,10,10):
    r = requests.get('https://www.indeed.com/jobs?q=python%20developer&start={}&vjk=a0c69a4cf04a5947'.format(number),headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('a',class_='tapItem')
    location = soup.find_all(class_='location')
    names = soup.find_all('div',{'class': 'slider_container'})
    for ti in names:
        href=ti.a['href']
        title1=ti.get_text()
        new_link = base_link + href
        
        title = ti.find('span').get_text()
        if title =='new':
            continue
        df.loc[len(df.index)] = [title,new_link]

#df['length'] = df['title'].apply(Lambda x: len(x.split(' ')))
#df.to_csv('jobs_indeed.csv')

payload_json= {

"content":new_link}

header = {
    'authorization': 'MzIxMzMzMzEyODIxOTE5NzQ1.YgqLfw.v1arRkTEIh18QdPc7VHTMBZkW40'
}

t = requests.post('https://discord.com/api/v9/channels/942828858435043351/messages', data = payload_json, headers=header)
