import requests
from bs4 import BeautifulSoup
import urllib.request

urlLaLibre = input("entrer le lien à extraire: ")
pageLaLibre = requests.get(urlLaLibre)
soupLaLibre = BeautifulSoup(pageLaLibre.content,"html.parser")
titleLaLibre = soupLaLibre.find_all("img")

c = 0
for i in titleLaLibre:
    urllib.request.urlretrieve(i["src"], str(c))
    c+=1