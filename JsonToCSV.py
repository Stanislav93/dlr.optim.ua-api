import csv

def canvert(dir, JsonProducts):

    with open(dir+'products.csv', 'w+', newline='\n') as csvfile_products:

        spamwriter = csv.writer(csvfile_products,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        with open(dir+'products_params.csv', 'w+', newline='\n') as csvfile_products_params:
        
            spamwriter_params = csv.writer(csvfile_products_params,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

            spamwriter.writerow([
                'product_id',
                'Подкатегория прайс-листа',
                'Тип',
                'Серия прайс-листа',
                'Категория',
                'Подразделение',
                'Подкатегория',
                'Наименование',
                'Артикул',
                'Бренд',
                'Описание',
                'Валюта РРЦ',
                'PPЦ',
                'Валюта дилерская',
                'Дилерская цена',
                'МИЦ',
                'Валюта МИЦ',
                'Параметри'
            ])

            spamwriter_params.writerow([
                'product_id',
                'name',
                'value'
            ])
            
            for product in JsonProducts:
                product_id = product
                product = JsonProducts[product_id]

                sp = product['structure_props']
                cp = product['common_properties']
                cps = product['category_props']
                prices = product['prices']

                product_data = [
                    product_id,
                    sp['PodkategoriyaPraysLista']['value'] if sp.get('PodkategoriyaPraysLista') else "",
                    sp['SvoystvoTip']['value'] if sp.get('SvoystvoTip') else "",
                    sp['SeriyaPraysLista']['value'] if sp.get('SeriyaPraysLista') else "",
                    sp['SvoystvoKategoriya']['value'] if sp.get('SvoystvoKategoriya') else "",
                    sp['SvoystvoOtdel']['value'] if sp.get('SvoystvoOtdel') else "",
                    sp['SvoystvoPodkategoriya']['value'] if sp.get('SvoystvoPodkategoriya') else "",
                    cp['Naimenovanie']['value'] if cp.get('Naimenovanie') else "",
                    cp['Articul']['value'] if cp.get('Articul') else "",
                    cp['NaimenovanieBrend']['value'] if cp.get('NaimenovanieBrend') else "",
                    product['description']['value'] if product.get('description') else "",

                    prices['VR']['value'] if prices.get('VR') else "",
                    prices['R']['value'] if prices.get('R') else "",
                    prices['VD']['value'] if prices.get('VD') else "",
                    prices['D']['value'] if prices.get('D') else "",
                    prices['M']['value'] if prices.get('M') else "",
                    prices['VM']['value'] if prices.get('VM') else ""                
                ]
                
                product_params_data = []
                for param in cps:
                    spamwriter_params.writerow([product_id,cps[param]['name'],cps[param]['value']])

                if product_data:
                    spamwriter.writerow(product_data)
    
    pass