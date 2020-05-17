from dir_optim_ua import DirOptimUA
import JsonToCSV
import JsonToYML

import config
print('Авторізаці: ...')
dou = DirOptimUA(config.username, config.password)

if dou.token:
    print('Авторізаці: Успішна! ;)')
    #print('Отримання Валтюи: ...')
    #currency = dou.getCurrency()

    #if currency:
    #    print('Отримання Валтюи: Успішно! ;)')

    print('Отримання Продуктів: ...')
    JsonProducts = dou.getPriceList({
        'payment_type':2,
        'user_price_option': 1,
        'brands': [342,344,426,362,374]})

    if JsonProducts:
        print('Отримання Продуктів: Успішно! ;)')
        if config.convertTypeFile == 'csv':
            print('Конвертація в файл CSV: ...')
            JsonToCSV.canvert(config.dir, JsonProducts)
            print('Конвертація в файл CSV: Успішно! ;)')
        
        if config.convertTypeFile == 'yml':
            print('Конвертація в файл YML: ...')
            JsonToYML.canvert(config.dir, JsonProducts)
            print('Конвертація в файл YML: Успішно! ;)')