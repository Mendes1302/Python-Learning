from os import system
from tqdm import tqdm
import googlesearch


class By:
    _sites = list()
    _ping = list()
    _name_search = list()

    def __init__(self, searching, linkedin, stop=2, tld="com.br", num=10, pause=2, checkping=0):
        self.searching = searching
        self.linkedin = linkedin
        self.stop = stop
        self.num = num
        self.pause = pause
        self.checkping = checkping
        self.tld = tld


    def check_ping(self, url):
        try:
            response = system("ping -c 1 " + url)
            system("clear")
            if response == 0:
                response = 1
            else:
                response = 0
            return response
        except Exception as error: 
            print(error)
            pass



    def __search_site(self, name):
        global _ping, _sites
        try:
            for url in googlesearch.search(name, tld=self.tld, num=self.num, stop=self.stop, pause=self.pause):
                url = str(url).replace("https://", "").replace("http://", "")
                url = url[:url.find("/")]
                if self.checkping == 1:
                    self._ping.append(self.check_ping(url))
                self._name_search.append(name)
                self._sites.append(url) 

        except Exception as error: 
            print(error)
            pass
    
    def __search_linkedin(self, name):
        global _ping, _sites
        try:
            for url in googlesearch.search(name+' Linkedin', tld=self.tld, num=self.num, stop=self.stop, pause=self.pause):
                if self.checkping == 1:
                    self._ping.append(self.check_ping(url))
                self._name_search.append(name)
                self._sites.append(url) 

        except Exception as error: 
            print(error)
            return 0



    def return_url(self):
        global _ping, _sites
        try:
            for value in tqdm(range(len(self.searching))):
                if self.linkedin:
                    ctrl = self.__search_linkedin(self.searching[value])
                    if ctrl == 0:
                        return 0
                else:
                    self.__search_site(self.searching[value])

            if len(self._ping):
                dict_return = {'URL': list(self._sites),
                                'Name': list(self._name_search),
                                'Status_ping':list(self._ping)}
            else:
                dict_return = {'URL': list(self._sites),
                                'Name': list(self._name_search)}
            return dict_return
            
        except Exception as error: 
            print(error)
            pass

