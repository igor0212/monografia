import requests

url = 'https://api.casamineira.com.br/busca/imoveis?finalidade=venda&tipos[]=apartamento&logradouros[]=logradouro_avenida-dos-engenheiros_belo-horizonte_mg'

r = requests.get(url = url)

data = r.json()

print(data)