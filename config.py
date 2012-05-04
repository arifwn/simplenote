'''
Base configuration module for SimpleNote.
'''

import base64
import json

evernote_host = 'https://sandbox.evernote.com/'

def get_api_key():
    '''
    Since this is an open source project, people will find out my key sooner
    or later, so there is no use to encrypt them. but I still don't want my key
    getting picked up by search engine easily ;)
    '''
    obfuscated_data = 'eyJFVkVSTk9URV9DT05TVU1FUl9LRVkiOiAiYXJpZnduIiwgIkVWRVJOT1RFX0NPTlNVTUVSX1NF\nQ1JFVCI6ICIyZmE2MGQ0OTAxMjg0NGM2In0=\n'
    return json.loads(base64.decodestring(obfuscated_data))
