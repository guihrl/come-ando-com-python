# import requests

# #URL da API
# url = "https://jsonplaceholder.typicode.com/users"

# #Fazendo a requisição GET para a API
# response = requests.get(url)

# #Verificando o status da requisição
# if response.status_code == 200:
#     #Convertendo a resposta em um objeto JSON
#     users = response.json()

#     for user in users:
#         if user['name'] == "Leanne Graham":
#             print(user)
#             print(f"Nome: {user['name']}, Email: {user['email']}")

# else:
#         print("Falha ao obter dados. Status code:", response.status_code)


import requests
import openpyxl

#URL da API
# url = "https://jsonplaceholder.typicode.com/users"

# #Fazendo a requisição GET para a API
# response = requests.get(url)

# #Verificando o status da requisição
# if response.status_code == 200:
#     users = response.json()
    
#     #Criando um arquivo Excel
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
    
#     #Adicionando os cabeçalhos das colunas
#     sheet.append(["ID", "Nome", "Email", "Empresa"])
    
#     #Adicionando os dados da ApI ao Excel
#     for user in users:
#         sheet.append([user['id'],user['name'], user['email'], user['company']['name']])
        
#     # Salvando o arquivo Excel
#     workbook.save("dados_api.xlsx")
#     print("Dados salvos com sucesso em dados_api.xlsx")
# else:
#     print("Falha ao obter dados. Status code:", response.status_code)

import requests


url = "https://loteriascaixa-api.herokuapp.com/api/lotofacil"
response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    for user in users:
        print(f" Data: {user['data']}, Valor Arrecadado: {user['valorArrecadado']}")

        