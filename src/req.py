import requests 

response=requests.get(url='http://127.0.0.1:5000/welcome')

print(response.content)

