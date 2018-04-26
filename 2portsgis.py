from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')

from selenium.webdriver.common.keys import Keys

driver.get('http://www.mainstreetmaps.com/ri/portsmouth/public.asp')

element = driver.find_element_by_id('d_disc_ok')
element.click()

##not working. obscured

#element = driver.find_element_by_class_name('lay_5')
#element.click()

task = driver.find_element_by_class_name('ui-autocomplete-input')

task.send_keys('104 Dighton AVE',Keys.RETURN,Keys.RETURN)
task.send_keys(Keys.RETURN,Keys.RETURN)

#driver.find_element_by_class_name('ui-autocomplete-input').send_keys('104 Dighton',Keys.ENTER)

#driver.implicitly_wait(3) # seconds

#element = driver.find_element_by_class_name('ui-menu-item')
#element.click()


#myDynamicElement = driver.find_element_by_id('d_disc')
#element = driver.find_element_by_id('d_disc')
#element.click()

#driver.find_element_by_id('s_location').send_keys(Keys.RETURN)
#driver.find_element_by_id('s_location').send_keys(Keys.RETURN)
#.sendKeys(u'\ue007')



