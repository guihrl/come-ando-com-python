#A sintaxe básica de um for em python




#Exemplo
# frutas = ["maçã", "banana", "laranja"]

#  for fruta in frutas:
#     print(fruta)

#A função reange() gera uma sequência de números, que é frequentemente utilizadas para laços for.:
#for i in range(5):  #traz do 0 ao 4
# o range(5) gera numéros de 0 a 4 (o último não é incluído)

#exemplo 2

# soma = 0
# for i in range(1,11): # traz umasequencia de 1 a 10
#     soma += i
#     print(soma)# se colocar o print dentro do laço ele mostra como ele fez para chegar até o final
# print(f"a soma de 1 a 10 é: {soma}")
# #Neste exemplo, o laço for é usado para somar os números de 1 a 10.

#exemplo 3
# palavra = "Python"
# for letra in palavra:
#     print(letra) #Neste caso, a variável letra assume cada caractere da string palavra

#desafio
# p = "Pythonnnnnn"

#  for i, z in enumerate(p):
#     print(f"A letra de {z} tem indice {i}")

#exemplo 4

# frase = input("digite uma frase: ").lower()
# vogais = "aeiou"
# contador = 0
# contador2 = 0

# for letra in frase:
#     if letra in vogais:
#         contador +=1
#     elif letra not in vogais:
#         contador2 +=1

# print(f"Há {contador} vogais na frase.")
# print(f"Há {contador2} conso... na frase.")
#----------------------------------------------------------------------------------------------


#Desafio Do prof
#ex 1
# for i in range(1,11):
#     print(i)

#ex 2
#soma = 0
#for i in range(1,50):
#    soma += i
#    print(soma)

#ex 3
# mult = 0
# frase = int(input("Digite um número: "))
# for i in range(1,11):
#     mult += 1
#     print(f"{frase}x{i} = {frase*mult}")

#ex 4
# pares = 0
# for i in range(1,21):
#     pares += 1
#     if pares %2 == 0:
#         print(pares)

#ex 5
# frase = "Python é divertido"
# palavras = frase.split()
# juntar = ''.join(palavras)
# letras = 0
# for frase in juntar:
#     letras +=1
#     print(f"{frase} {letras}")

#ex 6
# lista = [1, 2, 3, 4, 5]
# lista2 =[]

# for i in lista:
#     lista2.insert(0,i)
# print(lista2)

# #ex 7
# def encontrar_primos(n):
#     primos = []
#     for i in range(2, int(i))


#ex 8
# quadradoPerfeito = int(input("Digite um número: " ))
# total = quadradoPerfeito*quadradoPerfeito
# raiz = 0
# while = raiz*raiz< quadradoPerfeito


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A estrutura basica de um laço while

# while condicao:

#exemplo
# contador = 6 #quando eu coloco o contador = 6 ele coloca numeros infinitos

# while contador >= 5:
#     print(contador)
#     contador += 1
    
#Nesse exemplo, a variável contador é incrementada a cada interação
#Quando o valor de contador é maior que 5
#a condição do while deixa de ser verdadeira, e o laço é encerrado

#exemplo

# while True:
#     nome = input("Digite seu nome (ou 'sair' para para): ")
    
#     if nome == "sair":
#         break
#     print(f"Olá, {nome}")
    
#Nesse exemplo o programa continuará pedinto que o usuário para digitar seu nome até que ele digite "sair".
#O break é ultilizado para para a ação 

#exemplo 

# numero_secreto = 7
# tentativa = None

# while tentativa != numero_secreto:
#     tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    
# print("Parabéns você acertou o numero secreto")

# aqui o usuário vai ficar tentando até que acerte 

#ex 20

# import random
# minhaLista= ["guilherme", "carlos","uirá", "ruan","ribamar", "marcelo"]
# nome_secreto = random.choice(minhaLista)
# tentativa = " "


# while tentativa != nome_secreto:
#     tentativa = str(input("Na minha lista tem (guilherme, carlos, uirá, ruan, ribamar, marcelo) escolha: "))

# print("Parabéns você acertou o nome secreto")
#esse eu inportei o random para eu não saber qual é o número secreto

#exemplo
# contagem = 10

# while contagem > 0:
#     print(contagem)
#     contagem -=1
# print("feliz ano novo")

# while True:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operacao = input("Digite (+,-,x,/) ou 'sair' para parar: ")

#     if operacao == "+":
#         print(f"Resultado de {num1} + {num2} = {num1 + num2}")
#     elif operacao == "-":
#         print(f"O resultado de {num1} - {num2} = {num1 - num2}")
#     elif operacao == "x":
#         print(f"O resultado de {num1} x {num2} = {num1 * num2}")
#     elif operacao == "/":
#         if num2 != 0:
#             print(f"O resultado de {num1} ÷ {num2} = {num1 / num2}")
#         else:
#             print("Erro: Divisão pro zero.")
#     else:
#         print("Operação inválida!")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# numero_secreto = 1234
# tentativa = None

# while tentativa != numero_secreto:
#     tentativa = int(input("Adivinhe a senha com 4 digitos: "))

# print("Parabéns você acertou a senha!!")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# nunInserido = []
# soma = 0
# numInteiro = 0
# tentativa = None
# while tentativa != numInteiro:
#     numInteiro = int(input("digite um número inteiro: "))
#     if numInteiro == 0:
#         print(numInteiro)
#         print(nunInserido)
#         print(f"A soma dos números inseridos é: {soma}")
#         break
#     else:
#         nunInserido.append(numInteiro)
#         soma += numInteiro

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pares = 1

# while pares <=40:
#     if pares %2 == 0:
#         print(pares)
#     pares +=1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# nomes = []
# tentativa = None
# while tentativa != "sair":
#     tentativa = input("Digite um nome (ou 'sair' para encerrar): ")
#     if tentativa != "sair":
#         nomes.append(tentativa)
# print(nomes)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# dic = {}
# dic_compras = {"arroz":7.90, "feijao":8.50, "macarrão":4.50, "leite":4.80}

# print(dic_compras)

# dic_compras["cebola"] = 1.50

# print(dic_compras)

# del dic_compras["leite"]

# print(dic_compras)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
compras = []
while True:
    print("1 - adicionar")
    print("2 - remover")
    print("3 - exibir")
    print("4 - sair")
    print()
    adicionar = input("Digite sua lista de compras (ou 'sair' para encerrar): ")
    if adicionar == "1":
        produto = input("adicione um produto na sua lista: ")
        compras.append(produto)
        print(compras)
    elif adicionar == "2":
        print(compras)
        remover = input("Digite um item que você queira remover(quando terminar de remover digite 'parar' para encerrar)")
        compras.remove(remover)
        print("você removeu: ", remover)
    elif adicionar == "3":
        print(compras)
    else:
        break
    
print(f"Lista final: {compras}")