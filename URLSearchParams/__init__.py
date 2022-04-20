from urllib.parse import urlparse, parse_qs, urlencode

class URLSearchParams():
    def __init__(self, url : str) -> None : self.url = url
    def get(self, name : str) : return parse_qs(urlparse(self.url).query)[name][0] 
    def getAll(self) : return urlparse(self.url).query.split("&")
    def append(self, params : dict): 
        if "?" in self.url : return self.url+"&{}".format(urlencode(params))
        else : return self.url+"?{}".format(urlencode(params))
    def delete(self, name : str) : return 
