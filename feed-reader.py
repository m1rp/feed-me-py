import feedparser
import json
from dateutil.parser import parse
from pprint import pprint
from markdownify import markdownify

urls = []

with open('./urls.json') as url_file:
    urls = json.load(url_file)

feeds = [feedparser.parse(url)["entries"] for url in urls]

simplified_feeds = []
for index, feed in enumerate(feeds):
    simplified_feeds.append([])
    for f in feed:
        content = f.description if f.description else f.content[0].value
        simplified_feeds[index].append({
            'title':f.title,
            'content': markdownify(content),
            'link':f.link,
            "updated":f.updated
            })
            # not 100% sure I get this
    simplified_feeds[index].sort(key=lambda x: parse(x['updated']), reverse = True)

with open ("./feed.json", "w+") as file:
    file.write(json.dumps(simplified_feeds, indent = 4))