class Price_comparater():
    def __init__(self):
        self.__consult()
        self.dfs = None
        self.__read_arquives()
        return
        
    def __consult(self):
        url_aliexpress = 'https://pt.aliexpress.com/'
        url_mercado_livre = 'https://lista.mercadolivre.com.br/'
        product_item = 'rtx-3060'
        
        #Mercado Livre
        from scripts.mercado_livre import Mercado_Livre
        Mercado_Livre(link=url_mercado_livre,product=product_item).extract()

        #AliExpress
        from scripts.aliexpress import AliExpress
        AliExpress(url=url_aliexpress, product=product_item).extract()
    def __read_arquives(self):
        from pandas import read_excel, concat
        local_df = ['db/AliExpress.xlsx', 'db/Mercado_Livre.xlsx']
        dfs = []

        for i in local_df:
            x = read_excel(i)
            
            dfs.append(x)

        self.dfs = concat(dfs)
        
        return self.dfs

    def __filter(self):
        dfs = self.dfs.copy()
        dfs['PRICE'] = dfs['PRICE'].astype(float)
        dfs = dfs.loc[dfs['PRICE'] >= 1500]
        dfs = dfs[dfs['NAME'].str.contains('3060', case=False, na=False)]
        min_prices = dfs.groupby('LOCAL')['PRICE'].min().reset_index()
        min_prices = dfs.loc[dfs.set_index(['LOCAL', 'PRICE']).index.isin(min_prices.set_index(['LOCAL', 'PRICE']).index), ['NAME', 'PRICE', 'LINK']]
        
        return min_prices

    def extract(self):
        df = self.__filter()
        return df