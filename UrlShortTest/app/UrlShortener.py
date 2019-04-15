import re
import json
from app import UrlShortStore as DB
from app import UrlShortStatic

class UrlShortener:
    store = DB.UrlShortStore()
    def getShort(self, entries):
        short = ""
        for c in range(UrlShortStatic.shortLength):
            charMod = int(entries % len(UrlShortStatic.shortCharSet))
            entries = int(entries / len(UrlShortStatic.shortCharSet))
            indexShort = UrlShortStatic.shortLength - c - 1
            short = UrlShortStatic.shortCharSet[charMod] + short
        return short
    def validUrl(self,url):
        return not re.search(UrlShortStatic.validURIChars,url) and url[0:7] == 'http://'
    def addUrl(self,url):
        if self.validUrl(url):
            index = UrlShortener.store.addUrl(url)
            short = self.getShort(index)
            UrlShortener.store.setShort(index,short)
            return short
        else:
            raise Exception('Invalid Url')
    def getUrl(self,short):
        return UrlShortener.store.getUrl(short)
    def getRedirect(self,short):
        redirect = self.getUrl(short)
        return '<html><head><meta http-equiv="Refresh" content="0; url={}" /></head></html>'.format(redirect)
