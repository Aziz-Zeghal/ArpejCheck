from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
CHAT_IDS:[str] = os.getenv("CHAT_IDS").split(",")
TELEGRAM_MESSAGE = "🔥 L'appart est dispo 🔥"

#--| Setup
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

url = "https://www.arpej.fr/fr/residence/porte-ditalie-residence-etudiante-le-kremlin-bicetre/"
driver.get(url)
sleep(1)

def call():
    found = False
    max_retries = 10
    retries = 0 
    
    while not found and retries < max_retries:
        #First, we try to check if there is NO accomodation
        try:
            acc = driver.find_element(By.XPATH, "//p[@class='widget-ibail__desc widget-ibail__desc--over']")
            print("Nothing")
        #If we cannot find the container, an accomodation is there !
        except NoSuchElementException:
            #Add code to notify user
            print("Accommodation here!")
            send_telegram_alert()
            found = True
            driver.quit()
            return 0
        else:
            retries += 1
            sleep(10)
            driver.refresh()

    print("Accommodation not found or maximum retries reached.")
    driver.quit()

def send_telegram_alert():
    print("sending telegram messages:")
    for chat_id in CHAT_IDS:
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage?chat_id={chat_id}&text={TELEGRAM_MESSAGE}"
        print(requests.get(telegram_url).json()) # this sends the message


if __name__ == "__main__":
    call()
