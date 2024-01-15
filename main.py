# install selenium package
"""Selenium helps us to operate the web from our python"""
from selenium import webdriver
from selenium.webdriver.common.by import By

""" to prevent our browser from automatically closing, we use an option"""
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_element_cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# we can locate using xpath for file path
n = driver.find_element(By.XPATH, value='//*[@id="search-form"]/input[1]')

print(f"the price is ${price_element.text}.{price_element_cent.text}")

# we use quit to close the entire browser, while close closes a specific tab that is open
driver.quit()
# driver.close()