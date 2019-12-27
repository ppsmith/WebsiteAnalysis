import bs4
import download
import csv

def add(source, file, dirtyRoot, dict):  #source will be html file. File is the file that contains the adresses. Dict is lsit of addresses
    try:
        path = dirtyRoot + source
        with open(path) as data:
            html = data.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')

            for link in soup.find_all('a'):
                theLink = link.get('href')
                try:
                    if download.testLink(theLink, dict, dirtyRoot) == False:
                        print(f'The link: {theLink} could not be downloaded')
                        continue
                    download.addLinktoCSV(file, theLink)
                except Exception as e:
                    print(f'{theLink} could not be downloaded because {e}')
                    continue
    except Exception as e:
        return e

