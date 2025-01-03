class AliExpress():
    
    def __init__(self, url:str='url site', product:str = 'product_name'):
        self.url = url
        self.product = product
        self.site = None
        
        self.__consult()
                
    def __consult(self):
        from tool.web_scrapyng import Web_Scraping
        self.site = Web_Scraping()
        
        return self.site
    
    def __tratament(self):
        segunda_aba = self.site.ST(url=self.url).submit_input_box(input_tittle='search--keyword--15P08Ji', text_submit=self.product)
        bloco = self.site.BST(segunda_aba).get_all_elements('div',{'class':'multi--outWrapper--SeJ8lrF card-out-wrapper'},show=False)
        
        from pandas import DataFrame
        df = []
        
        for i in bloco:
            
            name = i.find('h3')
            name = name.text if name else '-'
            #print(f'PRODUCT_DESC : {name}')
            
            
            link = i.find('a', {'class': 'multi--container--1UZxxHY cards--card--3PJxwBm search-card-item'})
            href = link['href'] if link and 'href' in link.attrs else '-'
            link = f'https:{href}' if href.startswith('//') else href
            #print(f'LINK : {link}')
            
            
            price_div = i.find('div', {'class': 'multi--price-sale--U-S0jtj'})
            if price_div:
                spans = price_div.find_all('span')
                price = ''.join(span.text for span in spans)
            else:
                price = '-'
            #print(f'Preço: {price}')
            
            df.append({
                'NAME': name,
                'PRICE': price,
                'LINK': link,
                'LOCAL': 'ALI_EXPRESS'
            })   
            
        df = DataFrame(df)
        
        df['PRICE'] = df['PRICE'].astype(str)  
        df['PRICE'] = df['PRICE'].str.replace("R$", '', regex=False)  
        df['PRICE'] = df['PRICE'].str.replace('.', '', regex=False) 
        df['PRICE'] = df['PRICE'].str.replace(',', '.', regex=False)  
        df['PRICE'].astype(float)
        
        df.to_excel('db/AliExpress.xlsx',index=False)
        
        return df
    
    def extract(self):
        df = self.__tratament()
        
        return df