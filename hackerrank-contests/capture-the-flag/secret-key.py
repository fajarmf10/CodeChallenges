import json
from urllib.request import urlopen

json_str = urlopen('https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json').read().decode('utf-8')
json_dict = json.loads(json_str)
json_keys = json_dict.keys()
titles = []
for key in json_keys:
    url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/%s.json' % key
    response = urlopen(url)
    response = json.loads(response.read())
    titles.append(response['news_title'])
titles.sort()
for i in range(len(titles)):
    print(titles[i])