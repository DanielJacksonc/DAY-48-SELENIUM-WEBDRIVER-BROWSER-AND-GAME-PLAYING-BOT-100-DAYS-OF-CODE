"""This projecy challenges me to use Selenium to make a bot that plays the cookie game"""

# import all the neccesary modules. 1 imports the driver for the web, 2. imports By for accessing links,
# 3.accesses the funtions of Selenium like clicking.
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)


# get our cookie URL
driver = webdriver.Chrome(options=option)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

#Capture our cookie from the html inspection
cookie = driver.find_element(By.ID,"cookie")

# every five seconds, check which upgrades are available
#1. get the upgrades on selenium


items = driver.find_elements(By.CSS_SELECTOR,"#store  div")
item_id = [item.get_attribute("id") for item in items]
all_prices = driver.find_element(By.CSS_SELECTOR,"#store b")
#get time
timeout = time.time() + 5 #5 seconds
five_min = time.time() + 60*5  # 5 minutes


while True:
    cookie.click()

    #check if time is already five seconds to buy
    if time.time() > timeout:
        # get all upgrade for <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_price = []
        #convert all_prices to integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_price)):
                cookie_upgrades[item_price[n]] = item_id[n]

            # Get current cookie count
            money_element = driver.find_element(by=By.ID, value="money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that we can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()

            # Add another 5 seconds until the next check
            timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break













# driver.close()