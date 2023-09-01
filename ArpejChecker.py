from bs4 import BeautifulSoup
from time import sleep
from twilio.rest import Client

import keys
import requests

client = Client(keys.account_sid, keys.auth_token)

url = "https://www.arpej.fr/fr/residence/porte-ditalie-residence-etudiante-le-kremlin-bicetre/"

def call():
    found = False
    retries = 0 
    
    while not found :
        #First, we try to check if there is NO accomodation
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content,"html.parser")

        target_class = "widget-ibail__desc widget-ibail__desc--over"
        target = soup.find_all(class_ = target_class)
        
        if target == []:
            message = client.messages.create(
                to = keys.target_number,
                from_ = keys.twilio_number,
                body = "Found an accomodation here : " + link)
            found = True
            return 0
        print("try")
        retries += 1
        sleep(300)

call()
