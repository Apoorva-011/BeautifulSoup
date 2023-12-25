import requests
def fetchandsavetofile(url,path):
   r=requests.get(url)  
   with open(path,"w",encoding='utf-8') as f:
         f.write(r.text)
url="https://timesofindia.indiatimes.com/india/delhi"
fetchandsavetofile(url,"data/new.html")
