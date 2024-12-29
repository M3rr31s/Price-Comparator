class Requisition():
    
    def __init__(self, link, show_site='false'):
        self.link = link
        self.show_site = show_site
        self.__request()
        
    
    def __request(self):
        import requests
        
        self.cursor = requests.get(self.link)
        
        #Status Connection
        print(F'{10*"-"}\n STATUS_CONECTION : {self.cursor.status_code}.\n{10*"-"}')
        
        #Show HTML From Link
        def __show_site():
            from bs4 import BeautifulSoup
            
            content = self.cursor.content
            content = BeautifulSoup(content,'html.parser')
            return print(content.prettify())
                   
        if self.show_site == True:
            __show_site()
        
        return self.cursor
    
    def find_first_element(self, element_type = 'type', dic = {'type':'name'}, show=False):
        
        element = self.cursor.content
    
        from bs4 import BeautifulSoup
        element = BeautifulSoup(element, 'html.parser')
        element = element.find(element_type, dic)
        
        if show == True:
            print(f'{10*"-"}\n{element.prettify()}\n{10*"-"}')
        
        return element
    
    def find_all_elements(self, element_type = 'type', dic = {'type':'name'}, show=False):
        
        element = self.cursor.content
        
        from bs4 import BeautifulSoup
        element = BeautifulSoup(element, 'html.parser')
        element = element.findAll(element_type, dic)
        
        if show == True:
            for i in element:  
                print(f'{30*"-"}\n{i.prettify()}\n{30*"-"}')
                
        return element
        
        
