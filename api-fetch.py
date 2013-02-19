import sys
import json
from urllib2 import urlopen, quote

apikey = sys.argv[1]
tag = sys.argv[2]
output = file(sys.argv[3], 'w')

baseurl = 'http://content.guardianapis.com/%s.json?page-size=50'
contenturl = '%s?show-fields=body&api-key='+apikey

response = json.load(urlopen(baseurl % tag))
urls = [content['apiUrl'] for content in response['response']['results']]
for url in urls:
    try:
        print "Fetching %s" % url
        response = json.load(urlopen(contenturl % url))
        body = response['response']['content']['fields']['body']
        output.write(body.encode('UTF-8', 'replace')+'\n')
    except:
        pass
