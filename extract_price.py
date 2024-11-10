from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service("/home/varsha/Downloads/Python/chromedriver-linux64/chromedriver"))

driver.get("https://www.99acres.com/independent-house-in-chandigarh-ffid")

houses = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "tupleNew__outerTupleWrap")))

with open('extract_price.csv', 'a') as file:
    
    for house in houses:
        # Get house location
        location = house.find_element(By.CLASS_NAME, "tupleNew__locationName").text
        
        # Get house description
        description = house.find_element(By.CLASS_NAME, "tupleNew__bOld").text
        
        # Get house price
        price = house.find_element(By.CLASS_NAME, "tupleNew__priceValWrap").text
        
        # Get house area
        area = house.find_element(By.CLASS_NAME, "tupleNew__area1Type").text
        
        # Write the scraped data in the order of Location, Description, Price, Area
        file.write(f"\"{location}\",\"{description}\",\"{price}\",\"{area}\"\n")


time.sleep(5)

driver.quit()
