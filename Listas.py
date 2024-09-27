#não consigo recorrer Boleanos
#indice começa com 0 
#elemento começa com 1

# #Declarando uma lista vazia em python
# lista1 = []

# # lista1 = [1,"2",3] # Criando uma lista
# # print(type(lista1),lista1)

# # #Declaração de lista explícita
# # lista2 = list((1,"2",3))
# # # print(lista2)

# # # #Declaração implicita
# # lista3= ["C", 4.65, True, "true", "Vamos Aprender", ["outra","lista","interna" ],lista2]
# #print(lista3)

# lista4 = ["Primeiro","Segundo","Terceiro"]
# print(lista4)

#acessando um elemento da lista
# print(lista3)
# print(lista3[5][0]) #ACESSANDO A LISTA DENTRO DA LISTA

#**fatiando listas**

#nomeDaLista[start:stop:step]

#
#execute um print por vez

# print(lista3)
#  # o primeiro 2 significa start o numero 6 significa stop eo ultimo numero 2 é step
# print(lista3[2:6:2]) # o (len) ele trás o numero de todos os elementos da lista
# print(lista3[-1:])
# print("imprimindo dois em dois",lista3[::2])
# print(lista3[: :])
# print(lista3)
# print(len(lista3[5][2]))

#append adiciona elementos na lista
# lista1.append("Python")
# lista1.append("Java")
# lista1.append("Php")
# lista1.append("c#")
# print(lista1)

# #Inserir elementos em uma posição especifica
# lista1.insert(2, "C++")

# print(lista1)

# #remover um elemento pelo seu valor
# lista1.remove("Java")


# indice= lista1.index("Php")
# print(indice)

# #Remover um elemento pelo seu indice
# del(lista1[indice])
# print(lista1)

# print("lista original: ",lista4)

# #invertindo a lista
# lista4.reverse()
# print("Lista invertida: ", lista4)

# #Ordenando a lista
# lista4.sort()
# print("lista ordenada: ", lista4)


#Exercicio

# a= [1, 2, 3]
# b= a[:]
# b[0]= 5
# print(a[3]) #Da erro, porque eu nao tenho o indice 3


# minhaLista = [76, 92.3, "oi", True, 4, 76]

# minhaLista.append("pera")
# minhaLista.append("76")
# print(minhaLista)

# minhaLista.insert(3, "gato")
# print(minhaLista)

# minhaLista.insert(0, 99)
# print(minhaLista)

# lista = minhaLista.index("oi")
# print(lista)

# minhaLista.remove(True )
# print(minhaLista)

# uma_lista = [4,2,8,6,5]
# uma_lista = uma_lista + ["gato", "bode", "bola"]
# print(uma_lista)

#essa lista, mesmo achando que ia virar duas listas, nao acontece por que ela se concatena

umaLista = ["maçã", "banana", "laranja"]

umaLista.append("uva")
print(umaLista)

umaLista.remove("banana")
print(umaLista)

print(umaLista[2])

umaLista.reverse()
print("Lista invertida:", umaLista)