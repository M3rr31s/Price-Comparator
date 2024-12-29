class read_mercado_livre():
    
    def __init__(self, product,link):
        self.product = product
        self.link = link + self.product
          
    def __consult(self):
        
        from tool.request import Requisition
        site = Requisition(link=self.link,
                           show_site=False)
        
        return site
    
    def __tratment(self):
        
        site = self.__consult()
        
        content = site.find_all_elements('div',
                                         dic={'class':'ui-search-result__wrapper'},
                                         show=False)
        
        df = []

        for i in content:
            
            name = i.find('h2', {'class': 'poly-box poly-component__title'})
            name = name.text if name else '-'

            price_fraction = i.find('span', {'class': 'andes-money-amount__fraction'})
            price_fraction = price_fraction.text if price_fraction else "-"
            
            price_cents = i.find('span',{'class':'andes-money-amount__cents andes-money-amount__cents--superscript-24'})
            price_cents = price_cents.text if price_cents else "00"


            price = str(price_fraction) + "," + str(price_cents)
              
            link = i.find('h2', {'class': 'poly-box poly-component__title'})
            link = link.a['href'] if link and link.a else "-"

            


            df.append({
                'NAME': name,
                'PRICE': price,
                'LINK': link,
                'LOCAL': 'MERCADO_LIVRE'
            })

        from pandas import DataFrame
        df = DataFrame(df)

        df['PRICE'] = df['PRICE'].str.replace('.', '', regex=False).str.replace(',',".", regex=False)
        df['PRICE'].astype(float)
        df = df.sort_values(by='PRICE', ascending=True)
        
        return df
    
    def extract(self):
        
        x = self.__tratment()
        
        return x