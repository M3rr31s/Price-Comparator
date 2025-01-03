
class Mercado_Livre:
    
    def __init__(self, link:str, product:str):
        self.link = link
        self.product = product
        
        self.link = self.link + self.product
        
        self.__consult()
    
    def __consult(self):
        from tool.web_scrapyng import Web_Scraping
        self.site = Web_Scraping()
        self.html_content = self.site.ST(url=self.link).export_content()
        return self.html_content, self.site

    def extract(self):
        
        product_label = self.site.BST(content=self.html_content).get_all_elements('div', {'class':'ui-search-result__wrapper'})

        df = []

        for i in product_label:
            
            product_name = i.find('h2', {'class': 'poly-box poly-component__title'})
            product_name = product_name.text if product_name else '-'
            
            price_fraction = i.find('span', {'class': 'andes-money-amount__fraction'})
            price_fraction = price_fraction.text if price_fraction else "-"
            
            price_cents = i.find('span',{'class':'andes-money-amount__cents andes-money-amount__cents--superscript-24'})
            price_cents = price_cents.text if price_cents else "00"


            price = str(price_fraction) + "," + str(price_cents)
                
            link = i.find('h2', {'class': 'poly-box poly-component__title'})
            link = link.a['href'] if link and link.a else "-"
            
            df.append({
                'NAME': product_name,
                'PRICE': price,
                'LINK': link,
                'LOCAL': 'MERCADO_LIVRE'
            })    
            
        from pandas import DataFrame
        df = DataFrame(df)
        df['PRICE'] = df['PRICE'].astype(str)  
        df['PRICE'] = df['PRICE'].str.replace('.', '', regex=False) 
        df['PRICE'] = df['PRICE'].str.replace(',', '.', regex=False)  
        df['PRICE'].astype(float)
        
        df.to_excel('db/Mercado_Livre.xlsx',index=False)
        return