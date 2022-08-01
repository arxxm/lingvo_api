import requests

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'OWYyNGMyZDQtMjhmNy00OWViLWFmNzAtY2Y2ZTUzY2E1N2M2OjIwZmJiNTE0ZjhiZTQzYzI5MDIyYzE5ZjIyYzBmMjdh'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
print(auth.text)

if auth.status_code == 200:
    token = auth.text
    while True:
        word = input('Введите слово для перевода: ')
        if word:
            if word == 'stop the program':
                break
            headers_translate = {'Authorization': 'Bearer ' + token}
            params = {
                'text': word,
                'srcLang': 1033,
                'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найдено варианта для перевода')

else:
    print('Error!')
