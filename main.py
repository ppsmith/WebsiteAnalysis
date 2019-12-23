import download
import os
import createdict
import parse

path = 'C:\\Users\\ppsmith\\seekingAlphaData\\dict.csv'  #path for the main dictionary of website urls

#print(download.downLoadfromdict(path))  #download the data from the websites in the dict to the dirtyData directory

entries = os.listdir('C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\')  #get the files in the dirty directory

for entry in entries:  #for each entry, remove the html tags, and save the file to the cleanData directory
    print(parse.parseSoup('C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\' + entry))
    #print(parse.parse('C:\\Users\\ppsmith\\seekingAlphaData\\dirtyData\\' + entry))


