#Requests -> __request
from requests import get

#BeutifulSoup -> BST
from bs4 import BeautifulSoup

#Selenium -> ST
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Web_Scraping:
    
    def __init__(self):
        
        self._bst = None
        self._st = None
        
    @property
    def BST_class(self):
        if self._bst is None:
            self._bst = self.BST(self)
        return self._bst
    
    class BST:
        
        def __init__(self, content:object):
            self.content = content
            self.__get_content()
        
        def __get_content(self):
            self.content = self.content
            self.content = BeautifulSoup(self.content,'html.parser')
            return self.content
            
        def show_site(self):
            return print(self.content.prettify())
        
        def get_first_element(self, element_type:str, dic:dict, show=False):
            
            element = self.content.find(element_type, dic)
            
            if show != False:
                print(f'{10*"-"}\n{element.prettify()}\n{10*"-"}')
            

            return element
        
        def get_all_elements(self, element_type:str, dic:dict, show=False):
            
            element = self.content.find_all(element_type, dic)
            
            if show != False:
                for i in element:
                    print(f'{30*"-"}\n{i.prettify()}\n{30*"-"}')
            
            return element
    
    @property
    def ST_class(self):
        if self._st is None:
            self._st = self.ST(self)
        return self._st
    
    class ST:
        
        def __init__(self, url):
            self.url = url
            self.option = None
            self.__options()
            self.__get_nav()
        
        def __options(self):
            self.options = Options()
            self.options.add_argument("--headless")  # Abre o navegador em modo fullscreen
            return self.options
        
        def __get_nav(self):
            self.nav = webdriver.Chrome(options=self.options)
            self.nav.get(self.url)
            
            sleep(5)
            
            return self.nav
        
        def export_content(self):
            content = self.nav.page_source
            return content              
        
        def submit_input_box(self, input_tittle:str, text_submit:str):
            
            search_button = self.nav.find_element(By.CLASS_NAME,value=input_tittle)
            search_button.send_keys(text_submit)
            sleep(5)
            search_button.send_keys(Keys.RETURN)
            
            content = self.nav.page_source
            
            return content
              