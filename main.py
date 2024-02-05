from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Timer
import time
import datetime as dt
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
game_time = 600

time_interval = time.time() + 5
print(time_interval)


def buy_upgrades():
    money_driver = driver.find_element(By.XPATH,value='//*[@id="money"]')

    cursor_driver = driver.find_element(By.ID, value="buyCursor")
    cursor_text = cursor_driver.text
    cursor_cost = cursor_text.split()[2]

    grandma_driver = driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]')
    grandma_text = grandma_driver.text
    grandma_cost = grandma_text.split()[2]

    factory_driver = driver.find_element(By.XPATH,value='//*[@id="buyFactory"]')
    factory_text = factory_driver.text
    factory_cost = factory_text.split()[2]

    #print(money_driver.text)
    money = int(money_driver.text)

    if money >= int(factory_cost):
        factory_driver.click()
        print("buying factory")

    elif money >= int(grandma_cost):

        grandma_driver.click()
        print("buying gran")
    elif money >= int(cursor_cost):
        cursor_driver.click()



while game_time > 0:
    cookie_driver = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

    time_now = time.time()
    if time_now > time_interval:
        buy_upgrades()
        game_time -= 5
        time_interval = time_now + 5
    cookie_driver.click()


cps_driver = driver.find_element(By.XPATH,value='//*[@id="cps"]')
print(f"Total CPS: {cps_driver.text}")
#//*[@id="cps"]
driver.quit()