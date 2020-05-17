import requests
import json

class DirOptimUA():
    host = 'https://dlr.optim.ua/api/'
    token = ''
    username = ''
    password = ''

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.auth()

    def auth(self):
        r = requests.post(self.host+'api-token-auth/', data={'username': self.username, 'password': self.password}).json()
        if r.get('token'):
            self.token = r['token']
            return True
        else:
            print(r['non_field_errors'])
            return False

    def getPriceList(self,params):
        if self.token:
            r = requests.get(self.host+'pricelist/', headers={'Authorization': 'JWT %s' % self.token}, params=params).json()
            t = type(r)
            if t == str:
                r = json.loads(r)
            
            if r.get('detail'):        
                print(r['detail'])
                return False
            else:
                return r
        else:
            return False

    def getCurrency(self):
        if self.token:
            r = requests.get(self.host+'currency/', headers={'Authorization': 'JWT %s' % self.token}).json()
            t = type(r)
            if t == str:
                r = json.loads(r)
            
            if r.get('detail'):        
                print(r['detail'])
                return False
            else:
                return r
        else:
            return False