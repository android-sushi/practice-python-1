import feedparser
from pprint import pprint

creatorclip = feedparser.parse('https://creatorclip.info/')
ggeek = feedparser.parse('https://ggeek.me/')

creatorclip['feed'].pop('summary')
ggeek['feed'].pop('summary')

with open('../test/creatorclip.text', 'w', encoding='utf-8') as f:
    pprint(creatorclip, stream=f)

with open('../test/ggeek.text', 'w', encoding='utf-8') as f:
    pprint(ggeek, stream=f)
