#imports Beautiful soup and adds the ability to access webpages through requestions
from bs4 import BeautifulSoup
import requests
#Input your desired link below, the example uses google
link='https://www.google.com'
#Sends a request to the webpage and stores the response
pglink=requests.get(link)
#converts the webpage a Beautiful soup object that can be accesssed
page=BeautifulSoup(pglink.text,'html')

#Retrieve any links found in the webpage
for link in page.find_all('a'):
    print(link.get('href'))