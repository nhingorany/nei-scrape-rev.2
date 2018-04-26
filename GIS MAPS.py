#gis maps

import time
from time import sleep


from selenium import webdriver



from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

import time
from time import sleep
import datetime

from PIL import Image

import re
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys


print ("program search vision apprisal in Portsmouth, Middletown, Tiverton, Newport; gets gis and aerial")
print  ("if using Tiverton use full name e.g. road, way, lane")
print ("if using Portsmouth Middletown or Newport use abbrev. eg. RD, WAY, LN")
print ("litteral searches for address only - not for use with vacant land")
address = input("Enter Address")
town = input("Enter Town, no spaces, and capitalize first letter")
state = input("Enter Two Letter State")

print("open town page" + town)

driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')
driver = webdriver.Firefox()

if town == 'Portsmouth':
    gis = 'http://www.mainstreetmaps.com/ri/portsmouth/public.asp'
elif town == 'Tiverton':
    gis = 'http://www.mainstreetmaps.com/ri/tiverton/public.asp'
elif town == 'Newport':  #arcgis
    gis = 'http://newportri.maps.arcgis.com/apps/webappviewer/index.html?id=78f7978f5667474da76d2533481662e4'
elif town == 'Middletown':  #tighebond
    gis = 'http://hosting.tighebond.com/MiddletownRI_Public/index.html'
else:
    print ('you spelled the Town name wrong or did not capitalize dummy OR town not in gis index')

driver = webdriver.Firefox()
driver.maximize_window()

#town list
mainst = ["Portsmouth", "Tiverton", "Warren"]
arcgis = ["Newport"]
tighebond = ["Middletown"]

if town in mainst:
    print("Using MainStMaps GIS")
    driver.get(gis)
    print ("searching for")
    print (town)
    print (gis)
    element = driver.find_element_by_id('d_disc_ok')
    element.click()

    elem = driver.find_element_by_id('s_location')
    elem.clear()
    elem.send_keys(address)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

    elem = driver.find_element_by_id('baselayers')
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

    driver.get_screenshot_as_file('tempgis.png')
    print ("tempgis screenshot saved")
    
elif town in arcgis:   #arcgis search
    print("Using ARCGIS GIS")
    driver.get(gis)
    print ("searching for")
    print (town)
    print (gis)
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="esri_dijit_Search_0_input"]')  #click search bar
    element.click()
    element.send_keys(address)
    #elem.send_keys(Keys.UP)
    element.send_keys(Keys.RETURN)
    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="widgets_ZoomSlider_Widget_31"]/div[1]')  #one click zoom in
    element.click()
    element = driver.find_element_by_xpath('//*[@id="widgets_ZoomSlider_Widget_31"]/div[1]')  #one click zoom in
    element.click()
    element = driver.find_element_by_xpath('//*[@id="widgets_ZoomSlider_Widget_31"]/div[1]')  #one click zoom in
    element.click()
    time.sleep(3)
    
    driver.get_screenshot_as_file('tempgis.png')
    print ("tempgis screenshot saved")

elif town in tighebond:  #tighebond search   #lot more to to click easements, etc. LOT OF INFO
    print("Using tighebond GIS")
    driver.get(gis)
    print ("searching for")
    print (town)
    print (gis)
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="searchinput"]')  #click search bar
    element.click()
    element.send_keys(address)
    #elem.send_keys(Keys.UP)
    element.send_keys(Keys.RETURN)
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="tabbasemap"]/button/div')  #click layer bar
    element.click()
    element = driver.find_element_by_xpath('//*[@id="baseMapGallery"]/li[4]/a/img')  #click googlem map bar
    element.click()
    
    
    time.sleep(3)
    driver.get_screenshot_as_file('tempgis.png')
    print ("tempgis screenshot saved")

  
   
else:
    print("town not in gis list")

driver.quit()



#END GIS ---------------------------



