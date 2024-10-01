#A sintaxe básica de um for em python




#Exemplo
# frutas = ["maçã", "banana", "laranja"]

# for fruta in frutas:
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

# #desafio
# p = "Pythonnnnnn"

# for i, z in enumerate(p):
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

#ex 7



#ex 8
quadradoPerfeito = int(input("Digite um número: " ))
total = quadradoPerfeito*quadradoPerfeito




