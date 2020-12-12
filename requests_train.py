#! python3
import requests
import pprint
import json

url = 'https://httpbin.org/get?name=Peter'
url2 = 'https://httpbin.org/get' # post / put / delete / get
url3 = 'http://localhost/website_forURLLIBtests/posted_form.php'
url4 = 'https://krunker.io/social.html'
url5 = 'https://api.github.com/events'

# r = requests.get('https://httpbin.org/get?name=Peter')
# print(r.text)
# r = requests.head(url3)
# data = {"nick" : "kamikaze", "pass": "hardcoreTroller"}
# for i in r.headers:
#    print(f'{i} : {r.headers[i]}')
# r = requests.post(url2, data = m_data)
# r = requests.get(url4, params = {"p":"profile", "q":"johnDoe"})
# print(r.encoding)
# print(r.headers['content-type']) # or you can use: r.headers.get('content-type')
# ------------------------------------------------------------------------------
# EXAMPLES ACCORDING TO OFFICIAL DOCUMENTATION TRAINING:
# payload = {'nickname' : 'skater8', 'eMaiL': "trollingHardOnTheMoon@gg.gg"}
# payloads by get, note ? is added automatically:
# r = requests.get('https://httpbin.org/get', params = payload)
# print(r.url)

# JSON:
# r = requests.get('https://api.github.com/events')
# pprint.pprint(r.json())

# r.raw for RAW SOCKET RESPONSE:
# r = requests.get('https://api.github.com/events', stream = True)
# print(r.raw)
# print(r.raw.read(10))
# in general you should use a pattern like this to save what is being streamed to a file:
# with open('./file.txt', 'wb') as fd:
    # Response.iter_content will handle a lot of what you would otherwise
    # have to handle when using Response.raw directly.
    # for chunk in r.iter_content(chunk_size=128):
    #     fd.write(chunk)
# An important note about using Response.iter_content versus Response.raw. Response.iter_content will automatically decode the gzip and deflate transfer-encodings. Response.raw is a raw stream of bytes – it does not transform the response content. If you really need access to the bytes as they were returned, use Response.raw.

# CUSTOM HEADERS - some website will try to prevent our bots from reading, therefore use custom header:
# headers = {'user-agent' : '8off-app/0.0.1'}
# r = requests.get('https://api.github.com/events', headers = headers)
"""
# POST:
url = 'https://httpbin.org/post'
headers = {'user-agent' : '8off-app/0.0.1'} # <-- for fun only
payload = {'nick' : 'SlickRick', 'pass': 'manaLaCompre'}
r = requests.post(url, data = payload, headers = headers) # headers for fun only
print(r.text)
"""
"""
# MULTIPLE VALUES FOR EACH KEY: payload_tuples == payload_tuples2 (they are the same)
payload_tuples = [('KEY1', 'VAL1'), ('KEY1', 'VAL2')]
payload_tuples2 = {'key1': ['val1', 'val2']}
r = requests.post(url, data = payload_tuples)
r2 = requests.post(url, data = payload_tuples2)
print(r.text)
print("*" * 24)
print(r2.text)
"""

# SENDING JSON, note: just parameter to encode payload as json:
payload = {"JSON_KEY" : "JSON_VALUE"}
r = requests.post('https://httpbin.org/post', json = payload)
# print(r.text)
# YOU COULD ALSO DO A LONGER WAY BY ENCODING BY YOURSELF A JSON, but that means you will import json:
# r = requests.post(url, data = json.dumps(payload))
# print(r.text)
# !!! so use option A with parameter json = some_payload !!!
# Using the json parameter in the request will change the Content-Type in the header to application/json
"""
# POST a Multipart-Encoded File:
# It is strongly recommended that you open files in binary mode. This is because
# Requests may attempt to provide the Content-Length header for you, and if it does
# this value will be set to the number of bytes in the file. Errors may occur if you open the file in text mode.
url = 'https://httpbin.org/post'
files = {'file' : open('file.txt', 'rb')}
r = requests.post(url, files = files)
# print(r.text)
# You can set the filename, content_type and headers explicitly:
files = {'some_file' : ('file.txt', open('file.txt', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
r = requests.post(url, files = files)
print(r.text)
"""

# COOKIES:
url = 'https://httpbin.org/cookies'
r = requests.get(url)
# print(r.cookies) # <<-- you can see object cookie 
# print(r.cookies['example_cookie_name'])
# send your own cookies to the server, you can use the cookies parameter:
cookies = {'cookies_are' : 'online yum yummy'}
r = requests.get(url, cookies=cookies)
print(r.text)
