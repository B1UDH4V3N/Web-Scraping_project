#install libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import re
#connection to website
URL= 'https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iphone+15&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=e63bc871-2483-4fbe-8410-1a4b1bcd9ee5.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=ru1satxf400000001715528099985&qH=2f54b45b321e3ae5'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
page=requests.get(URL,headers=headers)

#extracting data

soup1=BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
# print(soup1)
#print(soup2)
title=soup2.find(class_='VU-ZEz').get_text()
# print("Item:",title)
pr=soup2.find(class_='Nx9bqj CxhGGd').get_text()
# print("Price:",pr)
rating=soup2.find(class_='XQDdHH').get_text()
# print("Rating:",rating)

#Cleaning and beautifying output
pr1 = int(re.sub(r'[^\d]', '', pr.strip()))

title1=title.strip()
rating1=rating.strip()
'''print("Title: ",title1)
print("Price: ",pr1[1:])
print("Rating: ",rating1)'''

