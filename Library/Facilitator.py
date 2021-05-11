from selenium import webdriver
from time import sleep, time

class easy:
    def __init__(self, opts="", url=""):
        try:
            self.driver = webdriver.Chrome(options=opts)
            self.connect = self.driver.get(url)
        except Exception as error:
            print(error)            

    def dinamic_delay(self, element="", kind="id", name_file="", tm=1):
        """
            Returns the element if it was found.

                :param element: str [name of element in CSS or HTML]

                :param kind: str [type of element in CSS or HTML]

                :param name_file: str [image file name]
                
                :param tm: int [about time of delay]

            :return txt:
        """
        
         
        for _ in range(10*tm):
            try:
                if "ID" == kind.upper():
                    txt = self.driver.find_element_by_id(element)
                elif "NAME" == kind.upper():
                    txt = self.driver.find_element_by_name(element)
                elif "CLASS" == kind.upper():
                    txt = self.driver.find_element_by_class_name(element)
                elif "SCREENSHOT" == kind.upper():
                    txt = self.driver.get_screenshot_as_file(name_file)
                else:
                    break
                return txt
            except Exception:
                sleep(0.1)
    def end(self, t=0):
        if time:
            sleep(t)
        self.driver.close()
