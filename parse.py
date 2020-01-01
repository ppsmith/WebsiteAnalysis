import re
from sys import exc_info
import bs4
import addFromPage
import emoji

goodTags = ['p', 'span']

def parseSoup(source, cleanRoot, dirtyRoot, addOthers = 0): 
    try:
        with open(source) as file:
            dirtyData = file.read()
            soup = bs4.BeautifulSoup(dirtyData, 'html.parser')

            [tag.decompose() for tag in soup('style')]  #remove all style tags and contents
            [tag.decompose() for tag in soup('script')]  #remove all script tags and contents
            [tag.decompose() for tag in soup('path')]  #remove all path tags and contents
            [tag.decompose() for tag in soup('span')]  # remove all path tags and contents
            [tag.decompose() for tag in soup('p class')]  # remove all path tags and contents
            [tag.decompose() for tag in soup('meta content')]  # remove all path tags and contents

            #[tag.decompose() for tag in soup('a class')]  # remove all path tags and contents
            #[tag.decompose() for tag in soup('a')]  # remove all path tags and contents

            path = str(source)  # start to make the file name for the clean file
            path = path.replace('\\', '')  # remove the slashes from the file name so that is is a clean file
            dirtyRoot = dirtyRoot.replace('\\', '')
            newAddress = path.replace(dirtyRoot, '')
            cleanFile = cleanRoot + newAddress  # cleanFile is the file path of the clean data.
            cleanFile = str(cleanFile)

            with open(cleanFile, 'a+') as destination:
                for tag in goodTags:  #for each good tag in the list,
                    add = soup(tag)
                    for entry in add:
                        startString = entry.contents[0]
                        newString = str(startString)
                        newString = newString.strip()
                        newString = newString.replace('\n', '')
                        newString = newString.replace('\t', '')
                        newString = newString.replace('\r', '')
                        newString = newString.lower()
                        newString = emoji.get_emoji_regexp().sub(r'', newString)
                        destination.write(newString)
            destination.close()

    except Exception:
        return exc_info()[0]











