import requests
from BeautifulSoup import BeautifulSoup as bs

class translator:

    def __init__(self, key):
        self.translateHeader = "https://translate.yandex.net/api/v1.5/tr/translate";
        self.detectHeader = "https://translate.yandex.net/api/v1.5/tr.json/detect"
        self.api_key = key

    def translate(self,text, target):
            data = { 'key' : self.api_key,
                'text' : text,
                'lang' : target
            }
            response = requests.get(self.translateHeader, data)
            returnText =bs(response.text)
            output = (returnText.find('text').text)
            print output
            return output

    def detectLanguage(self, text):
        data = {'key' : self.api_key,
        'text': text}

        response = requests.get(self.detectHeader, data)
        data = response.json()
        print(data['lang'])
        return data['lang']
