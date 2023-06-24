from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

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
            found = True
            driver.quit()
            return 0
        else:
            retries += 1
            sleep(10)
            driver.refresh()

    print("Accommodation not found or maximum retries reached.")
    driver.quit()

call()
