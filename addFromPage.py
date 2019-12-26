import bs4
import download
import csv

def add(source, file, dict, dirtyRoot):  #source will be html fild. File is the file that contains the adresses. Dict is lsit of addresses
    try:
        path = dirtyRoot + source
        with open(path) as data:
            html = data.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')
            with open(file, 'w+') as file:
                writer = csv.writer(file, lineterminator = '\n')

                for link in soup.find_all('a'):
                    theLink = link.get('href')
                    try:
                        if download.testLink(theLink, dirtyRoot) == False:
                            print (f'The link: {link} could not be downloaded')
                            continue
                        writer.writerows(theLink)
                    except Exception as e:
                        print(f'{theLink} could not be downloaded because {e}')
                        continue
    except Exception as e:
        return e

