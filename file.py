from partner import Partner
import asyncio
import requests

goal = 'venda'
type = 'apartamento'
city = 'belo horizonte'
location = 'bairros'

async def post(url):    
    response = await requests.post(url)
    return {'url': response.url, 'status': response.status}

async def main():
    tasks = []
    file = open("drafts/cidades2.txt", "r", encoding="utf8")
    line = file.readline()    
    while line:
        url = 'http://127.0.0.1:5000/api/partner/district?goal=venda&type=apartamento&name={}&city=belo horizonte'.format(line)
        print(url)
        task = asyncio.create_task(post(url))
        tasks.append(task)
        line = file.readline()        

    file.close()

    await asyncio.gather(*tasks)   

asyncio.run(main())