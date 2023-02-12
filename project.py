""" The Major Celestial Object DataBase """


import requests
from bs4 import BeautifulSoup


class CelestialObject():
    def __init__(self, userchoice):
        self._userchoice = userchoice
        self._url = f"https://theskylive.com/{userchoice}-info"
        self._source = requests.get(self._url).text
        self._scraper = BeautifulSoup(self._source, 'lxml')
        self.scraped = self._scraper.find("span")
        self.main = self.scraped.find('div', style="background-color:#000000")
        self.content = self.main.find("div", class_="content",style="clear:both;")
        self._maincontent = self.content.find("div", class_="main_content")
        self._label = self._maincontent.find_all("label")
        self.ar = self._maincontent.find_all("ar")
        self.labellist = []
        self.arlist = []
        for i in range(len(self._label)):
            for j in self._label[i]:
                self.labellist.append(str(j))
        for i in range(len(self.ar)):
            for j in self.ar[i]:
                self.arlist.append(str(j))
    @property
    def url(self):
        return self._url

    def visibility_sky(self):
        masterstring = f"{self.labellist[0]}: + {self.arlist[0]} | {self.labellist[1]}: {self.arlist[1]} | {self.labellist[3]}: {self.arlist[3]} "
        return masterstring

    def current_distance(self):
        masterstring = f"{self.labellist[5]}: + {self.arlist[4]} | {self.labellist[6]}: + {self.arlist[5]} km | {self.labellist[7]}: + {self.arlist[6]}"
        return masterstring

    def closest_approach(self):
        masterstring = f"Details of the closest approach between January 2013 and December 2100: [{self.labellist[8]}: + {self.arlist[7]} | {self.labellist[9]}: + {self.arlist[8]} km| {self.labellist[10]}: + {self.arlist[9]}]"
        return masterstring
    @property
    def userchoice(self):
        return self._userchoice
    @property 
    def label(self):
        return self._label

def main():
    userchoice: str  = input("Pick the planet (or the Sun) in our solar system and this program will pull up its database").strip().lower()
    choice = CelestialObject(userchoice)
    while True:
        databasetype = input("which data would you like to pull up? visibility (1), currentdistance (2) or closest approach (3)?")
        if databasetype == "1":
            print(choice.visibility_sky())
            break
        elif databasetype == "2":
            print(choice.current_distance())
            break
        elif databasetype == "3":
            print(choice.closest_approach())
            break
        else:
            print("invalid option")
            continue



if __name__ == "__main__":
    main()
