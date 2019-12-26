import download
import os
import parse
import addFromPage

entries = os.listdir('C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\')  #get the files in the dirty directory
dirtyRoot = 'C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\'
cleanRoot = 'C:\\users\\ppsmith\\seekingAlphadata\\cleanData\\'

dict = 'C:\\Users\\ppsmith\\seekingAlphaData\\dict.csv'  #path for the main dictionary of website urls

url = ["https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/", "https://nyt.com/", "https://www.wsj.com/", "https://www.wsj.com/news/world",
                    "https://www.wsj.com/news/economy", "https://www.wsj.com/news/business", 'https://www.reddit.com/r/finance/'
                      ,'https://www.cnn.com/business', 'https://www.washingtonpost.com/', 'https://www.wsj.com/news/opinion']

#print(download.downLoadfromdict(dict, dirtyRoot))  #download the data from the websites in the dict to the dirtyData directory



for entry in entries:  #for each entry, remove the html tags, and save the file to the cleanData directory
    print(addFromPage.add(entry, dict, url, dirtyRoot))
    #print(parse.parseSoup(dirtyRoot + entry, cleanRoot, dirtyRoot)


