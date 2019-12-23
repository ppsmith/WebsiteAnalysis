import re
import csv
import traceback
from sys import exc_info
import bs4

goodTags = ['p', 'span']

def parseSoup(source):
    try:
        myString = ''
        with open(source) as file:
            dirtyData = file.read()
            soup = bs4.BeautifulSoup(dirtyData, 'html.parser')

            [tag.decompose() for tag in soup('style')]  #remove all style tags and contents
            [tag.decompose() for tag in soup('script')]  #remove all script tags and contents
            [tag.decompose() for tag in soup('path')]  #remove all path tags and contents

            path = str(source)  # start to make the file name for the clean file
            path = path.replace('\\', '')  # remove the slashes from the file name so that is is a clean file
            newAddress = path.replace('C:UsersppsmithseekingAlphaDatadirtyData', '')
            cleanFile = "C:\\Users\\ppsmith\\seekingAlphaData\\cleanData\\" + newAddress  # cleanFile is the file path of the clean data.
            cleanFile = str(cleanFile)

            with open(cleanFile, 'w+') as destination:

                for tag in goodTags:  #for each good tag in the list,
                    add = soup(tag)
                    for entry in add:
                        startString = entry.contents
                        newString = ''.join(startString)
                        destination.write(newString + '\n')
            print('hello')
            destination.close()

    except Exception:
        return traceback.print_tb(None)


def parse(source):
    try:
        with open(source) as file:
            dirtyData = file.read()  #opening the dirty data

        path = str(source)  #start to make the file name for the clean file
        path = path.replace('\\', '')  #remove the slashes from the file name so that is is a clean file
        newAddress = path.replace('C:UsersppsmithseekingAlphaDatadirtyData', '')
        cleanFile = "C:\\Users\\ppsmith\\seekingAlphaData\\cleanData\\" + newAddress  #cleanFile is the file path of the clean data.

        cleanFile = str(cleanFile)

        with open(cleanFile, 'w+') as destination:
            s = re.sub('<[^<]+?>', '', str(dirtyData))  #s is the dirty data without html tags
            s = s.replace('\\n', '')  #reomve the new line tags from the file
            s = s.replace('{', '')
            s = s.replace('}', '')
            destination.write(s)  #write the parsed text into the destination dile
        return 0
    except:
        e = exc_info()[0]
        return e



