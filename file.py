import requests

goal = 'venda'
type = 'apartamento'
city = 'belo horizonte'
location = 'bairros'

file = open("drafts/cidades2.txt", "r", encoding="utf8")
line = file.readline()    
while line:
    url = 'http://127.0.0.1:5000/api/partner/district?goal=venda&type=apartamento&name={}&city=belo horizonte'.format(line)
    requests.post(url)    
    line = file.readline()        

file.close()

print('Acabou')