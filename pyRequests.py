'''
We will handle web requests here

'''
import requests

class webRequest():

    def __init__(self):
        pass
    
    def makeRequest(self,url):
        r = requests.get(url)
        print(r.json())