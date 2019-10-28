from bs4 import BeautifulSoup
import urllib.request as rqst
import pandas as pd

url = "https://finance.yahoo.com/quote/AAPL/history?ltr=1"

page = rqst.urlopen(url)

soap = BeautifulSoup(page.read())
# print(soap)

i=0
price={}
table = soap.find_all('tbody')[0]
for tb in table.find_all('tr')[:20]:
    apple = tb.find_all('span')
    price[i] = (apple[0].get_text(), apple[4].get_text())
    i+=1

apple_price = pd.DataFrame.from_dict(price,orient='index', columns=['Date', 'Close Price'])
print(apple_price)