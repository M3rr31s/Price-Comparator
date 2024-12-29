class read_amazon():
    
    def __init__(self, product,link):
        self.product = product
        self.link = link
          
    def __consult(self):
        
        from tool.request import Requisition
        site = Requisition(link=self.link,
                           show_site=True)
        
        print(self.link)
        
        return site
    
    def __tratment(self):
        
        site = self.__consult()
        
        content = site.find_all_elements('div',
                                         dic={'class':'ui-search-result__wrapper'},
                                         show=True)
        
        df = []

        from time import sleep
        for i in content:
            
            name = i.find('a', {'class': 'a-link-normal s-line-clamp-4 s-link-style a-text-normal'})
            name = name.text if name else '-'

            price_fraction = i.find('span', {'a-price-whole'})
            price_fraction = price_fraction.text if price_fraction else "-"
            
            price_cents = i.find('span',{'class':'a-price-fraction'})
            price_cents = price_cents.text if price_cents else "00"


            price = str(price_fraction) + "," + str(price_cents)
              
            link = i.find('a', {'class': 'a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal'})
            link = link.a['href'] if link and link.a else "-"

            


            df.append({
                'NAME': name,
                'PRICE': price,
                'LINK': link,
                'LOCAL': 'AMAZON'
            })
            
            sleep(5)
            
            
        from pandas import DataFrame
        df = DataFrame(df)

        #df['PRICE'] = df['PRICE'].str.replace('.', '', regex=False).str.replace(',',".", regex=False)
        #df['PRICE'].astype(float)
        #df = df.sort_values(by='PRICE', ascending=True)
        
        return df
    
    def extract(self):
        
        x = self.__tratment()
        
        return x