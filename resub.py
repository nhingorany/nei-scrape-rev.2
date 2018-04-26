import re

#sample
text = "Python for beginner is a very cool website"
pattern = re.sub("cool", "good", text)
print (pattern)


#condensed version of what im  trying to fix
bunk = """ 1.4  hey hey  \n rules /x zz apples\n xxxx
            smells like 1.4
            hello pants on the
            bob shelf \n"""
        



#all fail to weed out '\n' and replace it with space
match1 = re.findall('1.4(.*)1.4', bunk, re.DOTALL)
print (match1)

##FUKCING WORKS
p5 = re.sub("\n", " ", str(''.join(match1)))
print (p5)


for match in matches:
    p6 = re.sub("\n", "", match)
    print (p6)
