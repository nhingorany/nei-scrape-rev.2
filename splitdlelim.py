#works just need to get list from .text

import time
from PIL import Image
import pytesseract
import argparse
import re
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
import pathlib
import docx
import re
import os
from docx.enum.text import WD_LINE_SPACING
from docx.shared import Pt
from docx import Document
from docx.shared import Inches
import json
import datetime
from copy import deepcopy
from docx.shared import Pt
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_LINE_SPACING
import json

import datetime

    
driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')


print("Using VisionAppriasal Database")
#driver = webdriver.Firefox(executable_path=r'c:\gecko\geckodriver.exe')
#driver = webdriver.Firefox()

driver.get('http://gis.vgsi.com/portsmouthri/Parcel.aspx?Pid=4547')
driver.maximize_window()




time.sleep(2)


#_------------------------------------------------------------------
listbp =[]

for i in range (5):
    m = '//*[@id="MainContent_grdSales"]/tbody/tr['
    o = i + 2
    p = ']/td[4]'
    linkx = (m + str(o) + p)
    print (linkx)
    if len (linkx) > 0:
        n = driver.find_elements_by_xpath(linkx)
        n2 = driver.find_elements_by_xpath(linkx)
        print (str(n2))
        print (n)
        listbp.append(n)
        
            

print (listbp)
    
                                      
"""
//*[@id="MainContent_grdSales"]/tbody/tr[2]/td[4] = 1
//*[@id="MainContent_grdSales"]/tbody/tr[6]/td[4] = 5
"""

""" 
    if len(driver.find_elements_by_xpath('//*[@id="MainContent_grdSales"]/tbody/tr[6]/td[4]')) > 0: 
        bp5 = driver.find_element_by_xpath('//*[@id="MainContent_grdSales"]/tbody/tr[6]/td[4]').text
        print (bp5)
    else:
        bp5 = "x"
        book5 = "x"
        page5 = "x"
        print ('no bp4'

bps = ["101-101", "101/201"]
bps.append  ("303-303")
print (bps)

for a,b in enumerate(bps):
    print ("A" + str(a) + ": " + str(b))
    x = str(a) + str(b)
    print (str(x))

print ("x")
print (str(x))"""

"""bp1 = "101/101"
bp2 = "101/101/101"



try:
    book2, page2 = re.split("[-/]", str(bp2))
except ValueError:
    print ("Failure")
    book2 = "x"
    page2 = "x"
else:
    print ("Success")

print (book2)
print (page2)

bps = ["101-101", "101/201"]
bps.append  ("303-303")
print (bps)

z = re.split ("[-/]", str(bps))
print (z)

for item in z:
    print (z)

b1, p1, b2, p2,  = z
print (b1)
print (p2)


print (bp2)
print ('bp2')

bp1, bp2, bp3 = bps
print (bp1)
print (bp2)"""


"""for i in range (1,2):
    book2, page2, book1, page1, = re.str.split("[-/]", str(bp1), str(bp2))
print (book2)
print (book1)"""
