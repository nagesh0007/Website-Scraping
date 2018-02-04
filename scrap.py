import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime
quote_page= 'https://www.bloomberg.com/quote/SPX:IND'
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print name
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price
pe=open('index.csv','a')
writer=csv.writer(pe)
writer.writerow([name,price,datetime.now()])
