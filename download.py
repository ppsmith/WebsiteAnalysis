from urllib3 import request, PoolManager
import sys
import createdict
import csv
import bs4

#contains methods to dolwnload html of known webpages, or a specifc webpage


#url = ["https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/", "https://nyt.com/", "https://www.wsj.com/", "https://www.wsj.com/news/world",
       #"https://www.wsj.com/news/economy", "https://www.wsj.com/news/business"]  #starting urls. Keep in mind that this uis not the curretn state of URLs


#func. downloads the data for all links in the dictionary. path is the path for the dictionary, and the dirtyRoot is the file for the dirty data. From seed is an option. 1 if the dict is emtpy, 0 if the dict has entries
def downLoadfromdict(path, dirtyRoot, fromSeed = 1):
    try:
        if(fromSeed == 1):
            dictionary = createdict.create(path)  #creates an instanse of a new dictionary for links

            dictionary.createCSV()

            csv_file = open(dictionary.getCSVPath())  #opens the file specified above

            reader = csv.reader(csv_file)  #creates a reader to read the cile opened above

        if(fromSeed == 0):
            csv_file = open(path, 'r')
            reader = csv.reader(csv_file)

        for entry in reader:  #for each row in the dict
            if entry is None:  #ensure that row exists
                return

            try:
                http = PoolManager()  #start a pool manager
                s = ""
                s = s.join(entry)  #s is a string version of the entry in the csv row
                entry = s
                print(entry)
                data = http.request('GET', entry)  #request the webpage

                newAddress = entry.replace('/', '')  #remove the slashes from the website url
                newAddress = newAddress.replace('_', '')
                newAddress = newAddress.replace('=', '')
                newAddress = newAddress.replace('?', '')

                newAddress = newAddress.strip('https://')  #remove the beggining of the url

                filepath = dirtyRoot + newAddress + '.txt'  #make a new file path

                file = open(filepath, 'w+')  #open new file
                dataText = str(data.data)  #turn the data from the website into a string
                file.write(entry)  #write the address the data is from into the first entry of the csv
                file.write('\n')  #write a newline
                soup = bs4.BeautifulSoup(dataText, 'html.parser')
                file.write(soup.prettify())  #write the website data into the file
            except Exception as e:
                print(e)
                continue
    except:
        e = sys.exc_info()[0]
        print(e)


#func. donwlaods the data from the link given. Path is the location of the local dictionary, link is the link to try to download, dirtyRoot is the location of the flle for diirty data
def downLoadfromLink(path, link, dirtyRoot):
    try:
        http = PoolManager()
        data = http.request('GET', link)

        newAddress = link.replace('/', '')
        newAddress = newAddress.replace('_', '')
        newAddress = newAddress.replace('=', '')
        newAddress = newAddress.replace('?', '')

        newAddress = newAddress.strip('https://')

        filepath = dirtyRoot + newAddress + '.txt'

        file = open(filepath, 'w+')
        dataText = str(data.data)
        soup = bs4.BeautifulSoup(dataText, 'html.parser')
        dict = open(path, 'r')
        reader = csv.reader(dict)

        for entry in reader:
            if link == entry:
                return
            else:
                file.write(soup.prettify())

        dict.close()

        csv_file = open(path)
        writer = csv.writer(csv_file, lineterminator='\n')
        writer.writerow(link)

    except:
        e = sys.exc_info()[0]
        return e



#download func. that dowloads when testLink is run. Does not need to download because testLink passes it the neccesary stuff
def downloadFromTestLink(data, link, dirtyRoot):
    try:
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
def testLink(link, path, dirtyRoot, download = 1):
    try:
        dict = open(path, 'r')
        reader = csv.reader(dict)
        s =""
        for entry in reader:
            entry =  s.join(entry)
            if link == entry:
                return False

        http = PoolManager()
        data = http.request('GET', link)
        if(download == 0):return True
        if len(data.data) < 10: return False
        downloadFromTestLink(data, link, dirtyRoot)
        return True
    except Exception as e:
        return False


#func remvoes a link from the ditionary based on a file name.
def removeFileFromList(file, dict):
    return None

#func adds a link to the csvFile
def addLinktoCSV(csvPath, link):  #csvPath is path to the csv file, and link is the link that needs to be added
    file = open(csvPath, 'a')
    writer = csv.writer(file, lineterminator = '\n')
    writer.writerow(link)