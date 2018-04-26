import docx
import re


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



#print (fullText)

#finds text between two markers, 101, 101a
match1 = re.findall('101(.*?)101a', str(fullText), re.DOTALL)


#removes newline \n and prints TEXT!!!!
p5 = re.sub("\n", " ", str(''.join(match1)), re.DOTALL)
print (p5)



