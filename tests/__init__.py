import requests
import json

api = requests.get("https://covid19-brazil-api.vercel.app/api/report/v1/")

dados = api
dados = json.loads(dados.text)

nome = str(input("Digite o estado: "))

total = []

for estados in dados["data"]:
    if estados["state"] == nome:
        print(f'\nCasos em {nome}: \nContaminados: {estados["cases"]}\nSuspeitos: {estados["suspects"]}\nMortes: {estados["deaths"]}')

for estados in dados["data"]:
    total.append(estados["cases"])

print(f'Valor total no Brazil: {sum(total)}')

# for estados in dados["data"]:
#     print(estados["state"])