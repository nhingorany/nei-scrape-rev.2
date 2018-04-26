from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')

from selenium.webdriver.common.keys import Keys

url = 'http://gis.vgsi.com/portsmouthri/Search.aspx'
browser.get(url)
