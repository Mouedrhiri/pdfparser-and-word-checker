# PDF Parser To Look For a String Or A Word in a PDF By Mohammed Ouedrhiri

# Using Python

## Private University Of Fez

> (It's A University Project)

> Follow Me On Github For More Projects

> Mohammed Ouedrhiri &copy;

#### Linkedin Account [Linkedin](https://www.linkedin.com/in/mohammed-ouedrhiri-512183187 “Linkedin”)

# Lets Begin The explanation

## The Progress Bar :

### I've Creted The Progress Bar Using THE Tqdm (تقدم) and Import it

> `from tqdm import tqdm`

### Then Imported The Sleep Library To Control The Time Flow

> `from time import sleep`

## Open the pdf file:

First You Need To Import PDF Library

> `import PyPDF2`

And Then :

> `object = PyPDF2.PdfFileReader("test.pdf")`

## Get number of pages:

> `NumPages = object.getNumPages()`

## Define Key Terms:

> `String = input("Enter Your Desired Word : ")`

I've Also Created an Empty List to store The Page Numbers Where The Word Was Found

> `listofpages = []`

## Extract text and do the search:

I Created a Counter To Count How Much The World Found

    count = 0

Now The Search Begin

    for i in range(0, int(NumPages)):

To Get Pages

        PageObj = object.getPage(i)

To Extract Text

        Text = PageObj.extractText()

To Search The Text

        ResSearch = re.search(String, Text)

If The Resul Is None The Program Will Ignore it and Only Count When it's Found

        if ResSearch != None:
            print(f"We've Found It in Page {i} Hold On ")

Simply Count increment By One

            count+=1

And Add The Pages Numbers To Use Them Later

            listofpages.append(i)

Call The Progress Bar

            progress(PageObj)

Now We Will Print If Only The Word Found :

    if count > 1:
        print(f"We've Found The Word {count} times")
        print("We've Found it In These Pages : ")
        for i in range(len(listofpages)):
            print(f"In The Page Number {i}")
    else:
        print("We Didn't Found The Desired Element")
    print("Hope You Enjoyed Our Programme")

---

Thanks For Using My Code If You Have Any Problem Contact Me On email : mouedrhiri492@gmail.com

> Mohammed Ouedrhiri &copy;

![logo](https://www.laformation.ma/images/contenu/24214a91e4.png)
