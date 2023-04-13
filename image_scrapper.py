#here we will scrap the image from the web
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import logging
import pymongo
import os

#for saving this collected images in a directory
save_dir="images/"      
if not os.path.exists(save_dir):
  os.makedirs(save_dir)

#if our chrome does not block us from browsing we should use
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

#for taking the response
#for taking the response
query=input('Enter the name of the image that u want to scrap')
response = requests.get(f"https://www.google.com/search?q={query}&sxsrf=AJOqlzUuff1RXi2mm8I_OqOwT9VjfIDL7w:1676996143273&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiq-qK7gaf9AhXUgVYBHYReAfYQ_AUoA3oECAEQBQ&biw=1920&bih=937&dpr=1#imgrc=1th7VhSesfMJ4M")


#let us beautify it in html scraper so that we can scrap our data
soup=BeautifulSoup(response.content,'html.parser')

images_tag=soup.find_all("img")

#first image is nothing but related to web only so deleting it
del images_tag[0]

#for scrapping all the images one by one using a loop
img_data=[]
for i in images_tag:
  image_url=i['src']
  image_data=requests.get(image_url).content
  mydict={"index":image_url,"image":image_data}
  img_data.append(mydict)
  with open(os.path.join(save_dir,f"{query}_{images_tag.index(i)}.jpg"),"wb") as f:
    f.write(image_data)