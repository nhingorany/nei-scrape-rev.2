from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')

from selenium.webdriver.common.keys import Keys

driver.get('http://gis.vgsi.com/portsmouthri/Search.aspx')

driver.find_element_by_id('MainContent_txtSearchAddress').send_keys('104 Dighton')
driver.find_element_by_id('MainContent_txtSearchAddress').send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
element = WebDriverWait(driver, 5).until(
    lambda x: x.find_element_by_partial_link_text("Parcel"))

driver.find_Element_By_parial_link_text("Parcel").send_keys(Keys.Click)

#still can't find the link...
