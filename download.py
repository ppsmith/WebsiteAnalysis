from urllib3 import request, PoolManager
import sys
import createdict
import csv
import bs4

#contains methods to dolwnload html of known webpages, or a specifc webpage


url = ["https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/", "https://nyt.com/", "https://www.wsj.com/", "https://www.wsj.com/news/world",
       "https://www.wsj.com/news/economy", "https://www.wsj.com/news/business"]  #starting urls. Keep in mind that this uis not the curretn state of URLs

#func. downloads the data for all links in the dictionary. path is the path for the dictionary, and the dirtyRoot is the file for the dirty data
def downLoadfromdict(path, dirtyRoot):
    try:
        dictionary = createdict.create(path)  #creates an instanse of a new dictionary for links

        dictionary.createCSV()

        csv_file = open(dictionary.getCSVPath())  #opens the file specified above

        reader = csv.reader(csv_file)  #creates a reader to read the cile opened above

        for entry in reader:  #for each row in the dict
            if entry is None:  #ensure that row exists
                return

            http = PoolManager()  #start a pool manager
            s = ""
            s = s.join(entry)  #s is a string version of the entry in the csv row
            entry = s
            print(entry)
            data = http.request('GET', entry)  #request the webpage

            newAddress = entry.replace('/', '')  #remove the slashes from the website url

            newAddress = newAddress.strip('https://')  #remove the beggining of the url

            filepath = dirtyRoot + newAddress + '.txt'  #make a new file path

            file = open(filepath, 'w+')  #open new file
            dataText = str(data.data)  #turn the data from the website into a string
            file.write(entry)  #write the address the data is from into the first entry of the csv
            file.write('\n')  #write a newline
            soup = bs4.BeautifulSoup(dataText, 'html.parser')
            file.write(soup.prettify())  #write the website data into the file
    except:
        e = sys.exc_info()[0]
        return e


#func. donwlaods the data from the link given. Path is the location of the local dictionary, link is the link to try to download, dirtyRoot is the location of the flle for diirty data
def downLoadfromLink(path, link, dirtyRoot):
    try:
        http = PoolManager()
        data = http.request('GET', link)

        newAddress = link.replace('/', '')

        newAddress = newAddress.strip('https://')

        filepath = dirtyRoot + newAddress + '.txt'

        file = open(filepath, 'w+')
        dataText = str(data.data)

        for entry in url:
            if url == entry:
                return
            else:
                file.write(dataText)

        csv_file = open(path)
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow(link)

    except:
        e = sys.exc_info()[0]
        return e


#download func. that dowloads when testLink is run. Does not need to download because testLink passes it the neccesary stuff
def downloadFromTestLink(data, link, dirtyRoot):
    try:
        print('Inside Download')
        newAddress = link.replace('/', '')

        newAddress = newAddress.strip('https://')

        filepath = dirtyRoot + newAddress + '.txt'

        with open(filepath, 'w+') as file:
            soup = bs4.BeautifulSoup(data, 'html.parser')
            file.write(soup.prettify())
            print(f'File {filepath} created and written to!')

        return 'Data from link usccsesfully added to file'
    except Exception as e:
        print(e)


#func. allows us to test the validity of any new link. Returns false is the link cannot be donwloaded or already is in the our system. Returns true if the link can be downloaded and the data added to the library
def testLink(link, dirtyRoot):
    try:
        for entry in url:
            if link == entry:
                return False
        http = PoolManager()
        data = http.request('GET', link)
        downloadFromTestLink(data, link, dirtyRoot)
        return True
    except Exception as e:
        return False



#removes a specified link from the dictionary
def removeLinkFromList(link, file):
    try:
        for entry in url:
            if entry == link:
                url.remove(link)
        else:
            print(f"Link {link} not found in table. No links removed")
    except Exception as e:
        return e

#func remvoes a link from the ditionary based on a file name.
def removeFileFromList(file, dict):
    return None
