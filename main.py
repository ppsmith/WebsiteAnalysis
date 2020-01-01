import download
import os
import createSets
import parse
import addFromPage

entries = os.listdir('C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\')  #get the files in the dirty directory
dirtyRoot = 'C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\'
cleanRoot = 'C:\\users\\ppsmith\\seekingAlphadata\\cleanData\\'

dict = 'C:\\Users\\ppsmith\\seekingAlphaData\\dict.csv'  #path for the main dictionary of website urls

print(download.downLoadfromdict(dict, dirtyRoot, 0))  #download the data from the websites in the dict to the dirtyData directory

for entry in entries:  #for each entry, remove the html tags, and save the file to the cleanData directory
    #print(addFromPage.add(entry, dict, dirtyRoot, dict))
    print(parse.parseSoup(dirtyRoot + entry, cleanRoot, dirtyRoot))

