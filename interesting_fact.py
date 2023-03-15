import requests
import translate
url = 'http://numbersapi.com/'
translator = translate.Translator(to_lang='ru', from_lang='en')
while True:
    try:
        num = input(
            'Введите число для получения интересного факта\n')
        num = int(num)
    except:
        print('Неверный формат запроса!')
        continue
    result = requests.get(url + str(num))
    result = result.content.decode('utf-8')
    result = translator.translate(result)
    print(result)
    more = ''
    while more != 'n' and more != 'y':
        more = input('Еще? (у/n)\n')
    if more == 'y':
        continue
    else:
        break
