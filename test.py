import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://www.wikipedia.org")
driver.maximize_window()

elem = driver.find_element(By.ID, 'searchInput')
elem.send_keys('Juraj Dobrila')
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.CSS_SELECTOR, '#p-lang > div > ul > li.interlanguage-link.interwiki-hr.mw-list-item > a')
elem.click()

elem = driver.find_element(By.ID, 'ca-history')
elem.click()

elem = driver.find_element(By.CSS_SELECTOR, '#mw-history-search > legend')
elem.click()

time.sleep(10)

driver.close()

