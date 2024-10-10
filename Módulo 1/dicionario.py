#declarando dicionário

# dic= {}
# print(type(dic))
# dic_pessoas = {"Carlos":12345678910, "Guilherme":10987654321, "Marcelo":21345769801}
# print(dic_pessoas)

# #Adicionando um elemento no dicionário (chave: valor)
# #onde a chave é 'salgueiro' e o valor é 1.
# #A chave é passada dentro de colchetes, após o nome do dicionário.
# #                chave       valor
# dic_pessoas["Ribamar"] = 13265478901
# print(dic_pessoas)

# #buscando valor com base na chave

# cpf = dic_pessoas.get("Guilherme")
# print(cpf)
# print(f"O cpf de Guilherme é: {cpf}")

# #Remover um elemento com base na chave

# del dic_pessoas["Marcelo"]
# print(dic_pessoas)

# #pop Remove a chave e retorna o seu valor
# valor = dic_pessoas.pop("Ribamar")
# print("O valor da chave é : ",valor)
# print(dic_pessoas)

# #in Fala se a chave está no dicionário
# print("Guilherme" in dic_pessoas)

# #keys Pega todas as chaves do dicionário
# print(dic_pessoas.keys())

# #values Pega todos os valores do dicionário
# teste = dic_pessoas.values()
# print(teste)

# #Tem como transformar o dicionário em uma lista
# teste2 = list(dic_pessoas)

# print(teste2[1])

# #------------------------------------------------------------------------------------------------------------------------#
# dic_pessoas2 = {"Nascimento":54362123458, "Uirá": 22113265476, "Ruan": 53412376598}

# #popitem Ele remove e retorna o último elemento
# print(dic_pessoas2.popitem())
# print(dic_pessoas2)

# #update Mescla dois dicionário
# dic_pessoas.update(dic_pessoas2)
# print(dic_pessoas)

#---------------------------------------------------------------------------------------------------------------------------#
dic_portalAluno = {"nome":'Guilherme', "idade":17, "nota":10}
print(dic_portalAluno)

dic_portalAluno["curso"] = 'CienciadaComputação'
print(dic_portalAluno)

valor = dic_portalAluno.get("nome")
print(valor)

del dic_portalAluno["nota"]
print(dic_portalAluno)

print("idade" in dic_portalAluno)
