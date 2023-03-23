# pip install urllib3
import urllib3
# Buscar Dados da API
url = "https://api.github.com/users/psf/repos"
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.status)
print(response.data)

# Postar Dados da API
url = "https://httpbin.org/post"
http = urllib3.PoolManager()
response = http.request('POST', url, fields={'hello': 'world'})
print(response.status)