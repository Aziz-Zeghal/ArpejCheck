from bs4 import BeautifulSoup
from time import sleep
import requests

url = "https://www.arpej.fr/fr/residence/porte-ditalie-residence-etudiante-le-kremlin-bicetre/"

def call():
    found = False
    retries = 0 
    
    while not found and retries < max_retries:
        #First, we try to check if there is NO accomodation
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content,"html.parser")

        target_class = "widget-ibail__desc widget-ibail__desc--over"
        target = soup.find_all(class_ = target_class)
        
        if target == []:
            print("Accommodation here!")
            found = True
            return 0
        
        retries += 1
        sleep(300)

call()

