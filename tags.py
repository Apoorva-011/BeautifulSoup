import requests
from bs4 import BeautifulSoup
with open("sample.html","r") as f1:
    html_doc=f1.read()

soup = BeautifulSoup(html_doc,'html.parser')
#print(soup.prettify())
#print(soup.title.string)
#print(soup.div)
#print(soup.find_all("div")[0])
#for link in soup.find_all("a"):
 #  print(link.get("href"))
 #  print(link.get_text())
#a=soup.find(id="link")
#print(a.get("href"))
#print(soup.select("div.italic"))
#print(soup.select("span#lala"))
#print(soup.span.get("class"))
#print(soup.find(id="lala"))
#for child in soup.find(class_="container").children:
 # print(child)
#for parent in soup.find(class_="box").parents:
 #   print(parent) #container aur uska container body (i=i+1)
#cont=soup.find(class_="container")
#cont.name="span"
#cont["class"]="myclass class2"
#cont.string="U rock"
#print(cont)


#new tagss

#ultag=soup.new_tag("ul")

#litag=soup.new_tag("li")
#litag.string="home"
#ultag.append(litag)

#litag=soup.new_tag("li")
#litag.string="about"
#ultag.append(litag)

#soup.html.body.insert(0,ultag)

#with open("modified.html","w") as f:
  #  f.write(str(soup))

#cont=soup.find(class_="container")
#print(cont.has_attr("contentidtable"))

#def hasclassnotid(tag):
 # return tag.has_attr("class") and not  tag.has_attr("id")
#results=soup.find_all(hasclassnotid)
#print(results)
def hascontent(tag):
    tag.has_attr("content")
results=soup.find_all(hascontent)
for result in results:
    print(result)