from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def getCookiesTotal(elem):
    return int(elem.split("\n")[0].split(" "))


def getCookiesPerSecond(elem):
    return float(elem.split("\n")[1].split(":")[1].strip())


driver = webdriver.Chrome()
# Open a webpage
driver.get("https://orteil.dashnet.org/cookieclicker/")

try:
    consent_btn = driver.find_element(By.CSS_SELECTOR, 'body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button')
    consent_btn.click()
finally:
    print("consent was passed")
    time.sleep(0.5)

try:
    language_btn = driver.find_element(By.ID, 'langSelect-RU')
    language_btn.click()
finally:
    print("language was selected")
    time.sleep(1)

big_cookie = driver.find_element(By.ID, 'bigCookie')

cookies = driver.find_element(By.ID, "cookies")

while True:
    big_cookie.click()
    print(f"Cookies total: {getCookiesTotal(cookies.text)}")
    print(f"Cookies per second: {getCookiesPerSecond(cookies.text)}")
# driver.close()
