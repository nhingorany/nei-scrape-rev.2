import docx
import re
import os
from docx.enum.text import WD_LINE_SPACING

from docx import Document
from docx.shared import Inches
import json

import datetime
from copy import deepcopy



from docx.shared import Pt
from docx.shared import Pt
#reads docx and converts to text variable fullText
"""def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == '__main__':
    filename='NEI - MASTER PROPOSAL SCOPE - HOURLY RATES - NOTES 2018.docx';  #docx file name
    fullText=getText(filename)
    # print (fullText)"""

listx = ["101", "102", "103", "104"]

sectx = []
for i in sectx:
    while len(sectx) > 2:
        print ('enter value')
        s = input
        sect.append(s)
        print (sectx)
    else:
        print ('done')
        break

    

"""
cont = input ('enter Y/N')

if cont == "Y":
    sect2 = input ('enter sect2')
    match2 = re.findall(str(sect2) +'(.*?)' + str(sect2), str(fullText), re.DOTALL)  #adds section no.
    p2 = re.sub("\n", " ", str(''.join(match2)), re.DOTALL)
    print ('sect2')
    print (sect2)

if cont == "N":
    sect2 = "0"
    p2 = "0"
    print ('ok')
else:
    sect2 = "0"
    p2 = "0"
    print ('bad input - done')

print (sect2)
print (p2)"""
    
