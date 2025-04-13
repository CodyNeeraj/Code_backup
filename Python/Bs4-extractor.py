import requests 

from bs4 import BeautifulSoup 

def news(): 
    url='http://www.hindustantimes.com/top-news'
    resp=requests.get(url) 
    if resp.status_code==200: 
        print("Successfully opened the web page") 
        print("The news are as follow :-\n") 
        soup=BeautifulSoup(resp.text,'html.parser')     
        l=soup.find("ul",{"class":"searchNews"})
        for i in l.findAll("a"): 
            print(i.text)          
    else: 
        print("Error")       
news()
