import re

bp1 = "101/101"
bp2 = "101/101/101"



try:
    book2, page2 = re.split("[-/]", bp2)
except ValueError:
    print ("Failure")
    book2 = "x"
    page2 = "x"
else:
    print ("Success")

print (book2)
print (page2)

bps = ["101-101", "101/201/201"]

x = bps.re.split("[-/]")
print (x)
