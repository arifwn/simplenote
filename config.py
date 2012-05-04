'''
Base configuration module for SimpleNote.
'''

import base64
import json

API_ENDPOINT_URL = 'https://sandbox.evernote.com/'

def get_api_key():
    '''
    Since this is an open source project, people will find out my key sooner
    or later, so there is no use to encrypt them. but I still don't want my key
    getting picked up by search engine easily ;)
    '''
    obfuscated_data = 'eyJFVkVSTk9URV9BUElfS0VZIjogIjJmYTYwZDQ5MDEyODQ0YzYiLCAiRVZFUk5PVEVfQ09OU1VN\nRVIiOiAiYXJpZnduIn0=\n'
    return json.loads(base64.decodestring(obfuscated_data))
