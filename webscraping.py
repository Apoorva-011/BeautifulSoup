import requests
import pandas as pd
from bs4 import BeautifulSoup

url="https://www.amazon.in/s?k=ipad&crid=1U8UT5J6SMMID&sprefix=ipad%2Caps%2C217&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r=requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,'html.parser')
data={'title':[],'price':[]}
#print(soup.prettify())
spans=soup.find_all(class_="a-size-medium a-color-base a-text-normal")
#print(spans)
prices=soup.find_all(class_="a-price-whole")
for span in spans:
    print(span.string)
    data['title'].append(span.string)
for price in prices:
    # if not("a.ssls in price.get("class"))
    print(price.get_text())
    data['price'].append(price.get_text())
df=pd.DataFrame.from_dict(data)
df.to_csv("data.csv",index=False)
