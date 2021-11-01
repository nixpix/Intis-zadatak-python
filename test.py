import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def test_wikipedia_croatian_edit_history():
    driver = webdriver.Chrome()
    driver.get("http://www.wikipedia.org")
    driver.maximize_window()

    element = driver.find_element(By.ID, 'searchInput')
    element.send_keys('Juraj Dobrila')
    element.send_keys(Keys.RETURN)

    driver.find_element(By.CSS_SELECTOR, '#p-lang > div > ul > li.interlanguage-link.interwiki-hr.mw-list-item > a').click()
    driver.find_element(By.ID, 'ca-history').click()
    driver.find_element(By.CSS_SELECTOR, '#mw-history-search > legend').click()
    driver.find_element(By.CSS_SELECTOR, '#mw-input-date-range-to > div.mw-widget-dateInputWidget-handle').click()

    actions = ActionChains(driver)
    actions.send_keys('2020-07-01')
    actions.send_keys(Keys.RETURN)
    actions.perform()

    driver.find_element(By.CSS_SELECTOR, '#ooui-php-7 > button')
    #print(driver.find_element(By.CSS_SELECTOR, '#pagehistory > li.selected.before').text)
    assert '21:33, 24. travnja 2020.' in driver.find_element(By.CSS_SELECTOR, '#pagehistory > li.selected.before').text
    # == 'sadpret 21:33, 24. travnja 2020. Croxyz razgovor doprinosi 5.881 bajt +11 ukloni ovu izmjenu'

    driver.close()

