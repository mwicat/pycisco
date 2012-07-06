import requests

URL_EXECUTE = 'http://%(host)s/CGI/Execute'
URL_SCREENSHOT = 'http://%(host)s/CGI/Screenshot'

def execute(host, xml, user, password, headers={}):
    url = URL_EXECUTE % {'host' : host}
    data = 'XML=%s' % xml
    r = requests.post(url, data, auth=(user, password), headers=headers)

def screenshot(host, user, password, headers={}):
    url = URL_SCREENSHOT % {'host' : host}
    r = requests.get(url, auth=(user, password), headers=headers)
    return r.content

if __name__ == '__main__':
    import sys
    host = sys.argv[1]
    data = sys.stdin.read()
    execute(host, data, 'user', 'password')
