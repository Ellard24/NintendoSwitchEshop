'''
We will handle web requests here

'''
import requests
import json

class webRequest():

    def __init__(self):
        pass
    
    def makeRequest(self,url):
        r = requests.get(url)
        games = []
        if r.status_code == requests.codes.ok:
            return r.json()

    def makeList(self, data):
        info = {}