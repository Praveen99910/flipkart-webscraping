details = soup.find_all('div',class_ = "col col-7-12") #"col col-7-12" #"cPHDOP col-12-12"
details
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd 
import numpy as np
url = "https://www.flipkart.com/search?q=mobile%205g&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off"
#df = pd.read_csv(r'https://www.amazon.in/s?k=mobile+phone+under+30000&crid=1NWI1IXRERSW0&sprefix=mobile+phone+%2Caps%2C343&ref=nb_sb_ss_mvt-t11-ranker_5_13')
res = req.get(url)
res
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
responce = req.get(url, headers=headers)
responce
responce.content
soup = bs(responce.content, 'html.parser')
soup
details = soup.find_all('div',class_ = "col col-7-12") #"col col-7-12" #"cPHDOP col-12-12"
details
details = soup.find_all('div',class_ = "col col-7-12") #"col col-7-12" #"cPHDOP col-12-12"
details
details = soup.find_all('div',class_ = "col col-7-1") #"col col-7-12" #"cPHDOP col-12-12"
details
details = soup.find_all('div',class_ = "col col-7-12") #"col col-7-12" #"cPHDOP col-12-12"
details
phone_name = [i.div.text.split(' (')[0] for i in details]
phone_name
details = soup.find_all('div',class_ = "col col-7-12") #"col col-7-12" #"cPHDOP col-12-12"
details
%history -f WebScp_flipkart.py
