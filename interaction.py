from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
M = "Miracle no dey tire jesus"

common = webdriver.ChromeOptions()
common.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=common)
driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# find element by link text
total_articles = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# total_articles.click()

# Find element by their name
search = driver.find_element(By.NAME, "search")

# sending keyboard input to Selenium. we will do an import (from selenium.webdriver.common.keys import Keys
search.send_keys(M, Keys.ENTER)


# driver.close()