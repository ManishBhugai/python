from bs4 import BeautifulSoup
import requests

url="https://quotes.toscrape.com/"
API_KEY="78f4c10c4f1857128f3297a0e32645a7"

response=requests.get(url,timeout=10)
soup=BeautifulSoup(response.content,"html.parser")
dict={}
for quote in soup.select(".quote"):

    text=quote.select_one(".text").get_text(strip=True)
    author=quote.select_one(".author").get_text(strip=True)
    dict[text]=author
    
print(dict)
    



    

