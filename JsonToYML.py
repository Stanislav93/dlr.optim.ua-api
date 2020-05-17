
def replace_xml(tex):
    return str(tex).replace('&', '&amp;').replace('\'', '&apos;').replace('"', '&quot;').replace('>', '&gt;').replace('<', '&lt;')

def canvert(dir, JsonProducts):

    with open(dir+'products.xml', 'w+', newline='\n') as csvfile_products:

        yml = '<?xml version="1.0" encoding="utf-8"?>\r\n'
        yml += '    <yml_catalog date="2020-05-17 03:42">\r\n'
        yml += '        <shop>\r\n'
        yml += '            <name>ONLINE NAXODKA</name>\r\n'
        yml += '            <company>ONLINE NAXODKA</company>\r\n'
        yml += '            <url>https://onlinenaxodka.com</url>\r\n'
        yml += '            <currencies>\r\n'
        yml += '                <currency id="UAH" rate="1"/>\r\n'
        yml += '            </currencies>\r\n'
        yml += '            <categories>\r\n'
        yml += '                <category id=""></category>\r\n'
        yml += '            </categories>\r\n'
        yml += '            <offers>\r\n'

        categories = []

        for product in JsonProducts:
            product_id = product
            product = JsonProducts[product_id]

            offer = '               <offer id="'+product_id+'" available="true">\r\n'
            

            sp = product['structure_props']
            cp = product['common_properties']
            cps = product['category_props']
            prices = product['prices']
            remains = product['remains']

            price = str(prices['M']['value'] if prices.get('M') else '0').replace(',', '.')

            name = cp['Naimenovanie']['value'] if cp.get('Naimenovanie') else ""
            name = replace_xml(name)
            description = product['description']['value'] if product.get('description') else ""
            description = replace_xml(description)

            vendor = cp['NaimenovanieBrend']['value'] if cp.get('NaimenovanieBrend') else ""
            vendor = replace_xml(vendor)           

            offer += '                  <name>'+name+'</name>\r\n'
            offer += '                  <categoryId></categoryId>\r\n'
            offer += '                  <price>'+price+'</price>\r\n'
            offer += '                  <currencyId>UAH</currencyId>\r\n'
            offer += '                  <vendorCode>'+(cp['Articul']['value'] if cp.get('Articul') else "")+'</vendorCode>\r\n'
            offer += '                  <vendor>'+vendor+'</vendor>\r\n'
            offer += '                  <description>'+description+'</description>\r\n'

            quantity_in_stock = 0

            for quantity in remains:
                quantity_in_stock += float(quantity['value'])
            

            if quantity_in_stock:
                offer += '                  <quantity_in_stock>'+str(quantity_in_stock)+'</quantity_in_stock>\r\n'

            country = ''

            for param in cps:
                p_name = replace_xml(cps[param]['name'])
                p_value = replace_xml(cps[param]['value'])
                offer += '                  <param name="'+p_name+'">'+p_value+'</param>\r\n'
                if p_name == 'Країна виробник':
                    country = '                  <country>'+p_value+'</country>\r\n'
                    
            offer += country

            offer += '               </offer>\r\n'

            yml += offer

        yml += '            </offers>\r\n'
        yml += '          </shop>\r\n'
        yml += '  </yml_catalog>\r\n'

        csvfile_products.write(yml)