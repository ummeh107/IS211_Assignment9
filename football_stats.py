from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

rqst = urllib.request.urlopen("https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns")

soap=BeautifulSoup(rqst.read())
# print(soap.prettify())

i=0
players={}
for tr in soap.find_all('tr')[3:23]:
    td_list = tr.find_all('td')
    players[i]=(td_list[0].text,td_list[1].text, td_list[2].text,td_list[4].text)
    i+=1

touch_downs = pd.DataFrame.from_dict(players, orient='index',columns=['Name','Position', 'Team', 'Total Points']) 
print(touch_downs)