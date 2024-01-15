from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_option)
# driver.get(url="https://www.python.org/")
#
# event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
#
# events = {}
# for n in range(len(event_times)):
#     events[n]={
#         "name": event_names[n].text,
#         "date":event_times[n].text
#     }
# print(events)
#
# driver.quit()
# driver.close()


# ii decided to use OOP to solve this challenge.
class Questions:
    def man(self):
        F = input("Provide first name here : ")
        L = input("Provide Last name here : ")
        E = input("Provide Email here : ")
        # """"""""""""""""""""""CHALLENGE 3: using selenium to fill in a form"""""""""
        driver = webdriver.Chrome(options=chrome_option)
        driver.get(url="https://secure-retreat-92358.herokuapp.com/")

        #let me get for the sign up
        fname = driver.find_element(By.NAME,"fName")
        lname = driver.find_element(By.NAME,"lName")
        email = driver.find_element(By.NAME,"email")
        button = driver.find_element(By.XPATH, "/html/body/form/button")

        (fname.send_keys(F),lname.send_keys(L),email.send_keys(E),button.click())


        # button = driver.find_element(By.)



        # driver.close()