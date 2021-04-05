'''import requests
import sys


from bs4 import BeautifulSoup
import urllib.request

url= sys.argv[1]
username= sys.argv[2]
password= sys.argv[3]

def getrepourl(url,user,password):
    Content= requests.get(url, auth=(user,password))
    data=Content.data
'''

from bs4 import BeautifulSoup
import urllib2
import re
import urllib.request

url= sys.argv[1]
#username= sys.argv[2]
#password= sys.argv[3]

repoPage= urllib.request.urlopen(url)
page= BeautifulSoup(repoPage,"html.parser")

for link in page.find_all('a'):
    l=link.get("href")
    print(link.get("href"))
