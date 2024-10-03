# #Exemplo :

# def saudacao():
#     print("Olá, bem-vindo(a) à aula de funções em python")
    
#     #para 'chamar' a função e executar seu código:
# saudacao()

# #Exemplo

# def saudacao(nome):
#     print(f"Olá, {nome} bem-vindo(a) à aula de funções em python")
    
    
# saudacao("guilherme") #guilherme é um argumento

# #Exemplo

# def somar(a, b, c): #mais de um parametro
#     return a+b+c

# resultado = somar(10,20,30)
# print(resultado)

# #Exemplo 

# def checarNumero(n):
#     if n > 0:
#         return "Positivo"
#     elif n < 0:
#         return "Negativo"
#     else:
#         return "Zero"
# print(checarNumero(10))

# #Exemplo

# def saudacao(nome = "aluno"):
#     print(f"Ola,{nome}")
    
# saudacao(nome)
# saudacao("guilherme") #quando eu coloco esse parametro ele ignora "aluno" e  coloca "guilherme"

# #Tem como pedir para o usuário digitar
# def teste():
#     valor = int(input("Digite um número"))
#     if valor > 0:
#         return "Positivo"
#     elif valor < 0:
#         return "Negativo"
#     else:
#         return "Zero"
# teste()
# Isso não é uma boa prática, pois isso só iria aparecer só para o desenvolvedor e não para o usuário

#Exemplo

# globalVar = 100

# def exemploEscolpo():
#     localVar = "Estou dentro da funçao"
#     print(localVar)
#     print(globalVar)

# exemploEscolpo()
# print(localVar)
#Escopo de Variáveis:
#Escopo Local: Variáveis definidas dentro de uma função só existem dentro dela.
#Escopo Global: Variáveis definidas fora de qualquer função podem ser acessadas em qualquer parte do código.

#Exemplo 
#Argumento Posicional
#Os argumento são passados para a função na mesma ordem dos parâmetros

# def exibirNomeIdade(nome,idade):
#     print(f"Nome: {nome} Idade: {idade}")
    
# exibirNomeIdade(guilherme, 17)
# exibirNomeIdade(17, guilherme) # ele vai colocar Nome: 17 Idade: guilherme.

# #Argumentos Nomeados
# #Ao chamar a função, voçê especifica os nomes dos parâmetros

# def exibirNomeIdade(nome,idade):
#     print(f"Nome: {nome} Idade: {idade}")
    
# exibirNomeIdade(idade=17, nome="guilherme") #Não importa a ordem.

#Argumentos Arbitrários (*args e **kwargs):

# # *args: Recebe mútiplos argumentos como uma tupla.

# def somar_todos(*args):
#     return sum(args)
# print(somar_todos(1, 2, 3, 4, 5))

# # *kwargs: Recebe mútiplos argumentos nomeados como um dicionário.
# def exibir_detalhes(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave}: {valor}")
    
# exibir_detalhes(nome = "carlos", idade = 30, cidade = "São Paulo", telefone = "819923323120")

# #Função para encontrar a Soma de numéros pares usando "while"

# def soma_pares(numeros):
#     soma = 0
#     i = 0
#     while i < len(numeros):
#         if numeros[i] % 2 == 0:
#             soma += numeros[i]
#         i += 1
#     return soma

# print(soma_pares([1, 2, 3, 4, 5, 6]))

def obter_detalhes_pedido():
#Simula a obtenção de detalhes de um pedido
    pedido = {
        "item": "Notebook",
        "preco": 1200.00,
        "quantidade": 2

    }
    print("Detalhes do pedido obtidos.")
    return pedido

def calcular_preco_total(pedido):
#Calcula o preço total do pedido
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f"Preço total calculado: R${preco_total}")
    return preco_total

def enviar_confirmacao(pedido, preco_total):
# Simula o envio de uma confirmação de pedido
    print(f"Confirmação enviada para {pedido['quantidade']} {pedido['item']}(s).")
    print(f"Valor total a ser pago: R${preco_total}")

def processar_pedido():
#Chama as funções auxiliares para processar o pedido
    pedido = obter_detalhes_pedido()
    preco_total = calcular_preco_total(pedido)
    enviar_confirmacao(pedido, preco_total)

#Chamando a função principal
processar_pedido = obter_detalhes_pedido()