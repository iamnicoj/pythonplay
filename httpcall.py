import http.client

conn = http.client.HTTPSConnection("postman-echo.com")

payload = "{\"name\": \"sample\",\"time\": \"Wed, 21 Oct 2015 18:27:50 GMT\"}"

headers = {
    'user-agent': "vscode-restclient",
    'content-type': "application/json"
    }

conn.request("POST", "/post", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))