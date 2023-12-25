import requests
from bs4 import BeautifulSoup
import smtplib
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
pricelist=[]
def checkprice():
 url="https://www.amazon.in/s?k=iphone+13+pro+max&crid=2DXZ0SMMTBTLL&sprefix=iphone+13+pro+max%2Caps%2C275&ref=nb_sb_noss_1"
 r=requests.get(url,headers=headers)
 soup=BeautifulSoup(r.text,'html.parser')
 #print(soup.prettify()) <span class="a-price-whole">1,56,900</span>
 prices = soup.find(class_="a-price-whole")

 prices=float(prices.replace(",",""))
 #print(prices,type(prices))
 pricelist.append(prices)#each time we visit

def sendemail(message):
  s=smtplib.SMTP('smtp.gmail.com',587)
  s.starttls()
  s.login("tonymahna300@gmail.com","Approv@l19")
  s.sendmail("tonymahna300@gmail.com","apoorvamahna19@gmail.com",message)
  s.quit()

sendemail("hi")