import csv


class create:
    def __init__(self, path):
        self.__url = ["https://www.nytimes.com/section/business/economy", "https://www.nytimes.com/section/business/", "https://nyt.com/", "https://www.wsj.com/", "https://www.wsj.com/news/world",
                    "https://www.wsj.com/news/economy", "https://www.wsj.com/news/business"]  #starting urls. Keep in mind that this uis not the curretn state of URLs
        self.__path = path

    def createCSV(self):  #should only be run if you want a brand new csv with just the basic links
        csv_file = open(self.__path, 'w+')
        writer = csv.writer(csv_file, lineterminator = '\n')
        writer.writerows(self.__url)


    def getCSVPath(self):
        return self.__path


    def getURLDict(self):
        return self.__url

