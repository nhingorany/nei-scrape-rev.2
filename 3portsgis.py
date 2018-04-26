from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

driver.get('http://www.mainstreetmaps.com/ri/portsmouth/public.asp')

element = driver.find_element_by_id('d_disc_ok')
element.click()

driver.implicitly_wait(4) # seconds

elem = driver.find_element_by_id('s_location')
elem.clear()
elem.send_keys('104 Dighton')
elem.send_keys(Keys.UP)
elem.send_keys(Keys.RETURN)






driver.implicitly_wait(5) # seconds

#element = driver.find_element_by_class_name('ui-menu-item')
#element.click()

#elem.send_keys(Keys.RETURN)

#driver.find_element_by_id('s_location').send_keys(Keys.RETURN)

#driver.find_element_by_id('s_location').send_keys('104 Dighton'))
#driver.find_element_by_id('s_location').send_keys('104 Dighton'))


