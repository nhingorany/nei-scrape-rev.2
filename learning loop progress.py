import re

fullText = "101 is the mother fucking man 101 apples poop"

print('Please enter values for the list, one value per line')
print('Enter "done" (without the quotes) to end the list')

sect = []
while True:
    s = input('value: ')
    if s == 'done':
        break
    sect.append(s)

print('Here is the list:')
print(sect)

new = []
for item in sect:
    if len(item) > 2:
        print (item)
        print ('bobo')
        m = re.findall('sect(.*?)sect', str(fullText), re.DOTALL)
        print (m)  # may be join issue
    else:
        print ('no data')
        break
    new.append(m)
        
    

print ('done')


"""sep = '-'
split_list = []
for item in sect:
    if item == sep:
        split_list.append([item])
    else:
        split_list[-1].append(item)

print (split_list)

words = [line.split() for sect in lines]"""

"""
for i in sect:
    while True:
        book, page = re.split("[-/]", str(sect))
    else:
        break"""
    

"""
for line in sect
    re.findall('sect(.*?)sect', str(fullText), re.DOTALL)


my_regex = r"\b(?=\w)" + re.escape(TEXTO) + r"\b(?!\w)"
re.search(r"\b(?=\w)TEXTO\b(?!\w)", subject, re.IGNORECASE)"""
        

#match1 = re.findall('101(.*?)101a', str(fullText), re.DOTALL)


"""count = 0
sect = []
while len(sect) == 3:
    print ('enter 3 digit section or N to stop')
    sect.append(str(input()))
    print ('next')
    count = count +1
else:
    print ('done')"""
    



"""if len(bp1) >= 3:    
    book1, page1 = re.split("[-/]", bp1)
    print ("book_" + book1)
    print ("page_" + page1)
else:
    print ('no data')"""

"""
try:
    sect = []
    while True:
        print ('enter section no, enter N to stop')
        sect.append(str(input()))
except:
    print(sect)


for x in sect:
    if len(x) == 3:
        print (x)"""
        

#match1 = re.findall('101(.*?)101a', str(fullText), re.DOTALL)


"""

from copy import deepcopy
from docx.shared import Pt
from docx.shared import Pt
#reads docx and converts to text variable fullText
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == '__main__':
    filename='NEI - MASTER PROPOSAL SCOPE - HOURLY RATES - NOTES 2018.docx';  #docx file name
    fullText=getText(filename)
    # print (fullText)


##############################

sect1 = input("Enter Section1")

cont = input ("do you want to add another Y/N")

###################


#print (fullText)

#finds text between two markers, [INPUT SECTION]
match1 = re.findall('101(.*?)101a', str(fullText), re.DOTALL)


#removes newline \n and prints TEXT!!!!
p5 = re.sub("\n", " ", str(''.join(match1)), re.DOTALL)
print (p5)"""
