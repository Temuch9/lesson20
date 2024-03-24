import requests
import pprint


url = 'https://github.com/'
token = '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'



session = requests.session()
session.auth = ('Temuch9', token)


url = 'https://api.github.com/search/code?q=eval+in:file+user:ubi22'
result = session.get(url)
pprint.pprint(result.json())