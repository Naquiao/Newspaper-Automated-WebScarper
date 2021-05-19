import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime

html = requests.get('http://www.losandes.com.ar')
soup = BeautifulSoup(html.text, 'html.parser')
h1 = soup.find_all('h1', {'class': 'article-title'})
h2 = soup.find_all('h2', {'class': 'article-title'})
mycsv = open('links.csv', 'w')
fieldnames = ['titulares', 'link']
writer = csv.DictWriter(mycsv, fieldnames= fieldnames)
writer.writeheader()
for link in h1 and h2:
  mylink = BeautifulSoup(str(link), 'html.parser')
  gettinglink = mylink.find('a', href=True)
  writer.writerow({'titulares': str(gettinglink.find(text=True)),
                   'link': str(gettinglink['href'])})
mycsv.close()
print('csv has been generated')  
df = pd.read_csv('links.csv')
df['fecha']= datetime.today().strftime('%Y-%m-%d')
df['diario'] = 'Los Andes'
df.to_csv(path_or_buf='C:\\Users\\nacho\\repositorios\\Newspaper-Automated-WebScarper\\csv_scaped\\los_andes.csv')
