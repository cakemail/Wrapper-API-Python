import urllib, urllib2, json

class API:

    url = 'https://api.wbsrvc.com/'

    def __init__(self, key):
        self.header = dict(apikey=key)

    def call(self, method, params):
        request = urllib2.Request(
            self.url + method[0] + '/' + method[1],
            urllib.urlencode(params),
            self.header
        )
        try:
            response = json.loads(urllib2.urlopen(request).read())
            return response
        except urllib2.HTTPError as error:
            return dict(Error=str(error))
        