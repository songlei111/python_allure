import  requests

response = requests.get(url="https://www.baidu.com")

print(response.status_code)
print(response.cookies)


