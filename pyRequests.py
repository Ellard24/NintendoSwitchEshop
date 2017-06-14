'''
We will handle web requests here

'''
import requests
import json
import feedparser

class webRequest():

    def __init__(self):
        pass
    
    def makeRequest(self,url):
        r = requests.get(url)
        games = []
        if r.status_code == requests.codes.ok:
            return r.json()

    def getFeed(self, url):
        info = []
        feed = feedparser.parse(url)
        for key in feed["entries"]:
            #print(key["title"])
            info.append(key["title"])
            #print(key["link"])
        return info