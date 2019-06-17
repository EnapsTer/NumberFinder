import phonenumbers
import requests
from phonenumbers import geocoder

class PhoneNumberFinder():

    def __init__(self, url):
        self.url = url

    def get_number(self):
        #Download web page
        r = requests.get(self.url)
        if (r != None):
            try:
                text = r.content.decode('utf-8')
            except UnicodeDecodeError:
                return ['%s page have a decode problem' % self.url]
        else:
            return ['Page not found']
        context = []
        #find numbers in web page
        for match in phonenumbers.PhoneNumberMatcher(text, "RU"):
            #get phone numbers


            number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
            ch_number = phonenumbers.parse(number, "RU")
            geo = geocoder.description_for_number(ch_number, "ru")
            if geo == '':
                geo = 'Russia'
            context.append(number + ' region ' + geo + ' from ' + self.url)
            #return list with found numbers
        return set(context)

