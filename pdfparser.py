from tqdm import tqdm
from time import sleep
import PyPDF2
import re

def progress(prog):
    for i in tqdm(prog, desc ="Progress : "):
        sleep(.1)

object = PyPDF2.PdfFileReader("test.pdf")

NumPages = object.getNumPages()

String = input("Enter Your Desired Word : ")

listofpages = []

count = 0
for i in range(0, int(NumPages)):
    PageObj = object.getPage(i)
    Text = PageObj.extractText() 
    ResSearch = re.search(String, Text)
    if ResSearch != None:
        print(f"We've Found It in Page {i} Hold On ")
        count+=1
        listofpages.append(i)
        progress(PageObj)
if count > 1:
    print(f"We've Found The Word {count} times")
    print("We've Found it In These Pages : ")
    for i in range(len(listofpages)):
        print(f"In The Page Number {i}")
else:
    print("We Didn't Found The Desired Element")
print("Hope You Enjoyed Our Programme")
input() 