from urllib3 import request, PoolManager
import sys
import createdict
import csv

#contains methods to dolwnload html of known webpages, or a specifc webpage


url = ["https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/", "https://nyt.com/", "https://www.wsj.com/", "https://www.wsj.com/news/world",
       "https://www.wsj.com/news/economy", "https://www.wsj.com/news/business"]  #starting urls. Keep in mind that this uis not the curretn state of URLs


def downLoadfromdict(path):
    try:
        dictionary = createdict.create(path)  #creates an instanse of a new dictionary for links

        dictionary.createCSV()

        csv_file = open(dictionary.getCSVPath())  #opens the file specified above

        reader = csv.reader(csv_file)  #creates a reader to read the cile opened above

        for entry in reader:
            if entry is None:
                return
            http = PoolManager()
            s = ""
            s = s.join(entry)
            entry = s
            print(entry)
            data = http.request('GET', entry)

            newAddress = entry.replace('/', '')

            newAddress = newAddress.strip('https://')

            filepath = 'C:\\Users\\ppsmith\\seekingAlphaData\\' + newAddress + '.txt'

            file = open(filepath, 'w+')
            dataText = str(data.data)
            file.write(entry)
            file.write('\n')
            file.write(dataText)
    except:
        e = sys.exc_info()[0]
        return e

def downLoadfromLink(link, path):
    try:
        http = PoolManager()
        data = http.request('GET', link)

        newAddress = link.replace('/', '')

        newAddress = newAddress.strip('https://')

        filepath = 'C:\\Users\\ppsmith\\seekingAlphaData\\' + newAddress + '.txt'

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


def removeFromList(link, file):
    for entry in url:
        if entry == link:
            url.remove(link)
    else:
        print(f"Link {link} not found in table. No links removed")