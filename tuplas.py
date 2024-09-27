#Uma tupla é uma estrutura de dados imutaveis, mais pode manusea-la usando o indice de cada elemento

# tupla = (1,2,3,"quatro")
# print(tupla[0]) #output: 1
# print(tupla[3]) #output: quatro

# #tem como concatenar tuplas

# tupla1 = (1,2,3)
# tupla2 = (4,5,6)

#Tem como desenpacotar uma tupla
# tuplaa = (1,2,3)
# a,b,c = tuplaa
# print(a)
# print(b)
# print(c)

# #Tem como verificar se um elemento está em uma tupla

# tuplaa = (1,2,3)
# print(2 in tupla) # esse vai dar true, pois existe 2 na tupla
# print(4 in tupla) # esse vai dar false, pois não existe 4 na tupla

# #count ele conta quantos elementos tem na tupla
# tupla = (1,2,3,2,3,3)
# print(tupla.count(2)) # esse vai dar True, pois tem dois 2 na tupla
# print(tupla.count(4)) #esse vai dar False, pois não tem nemhum 4 na tupla

cores = ("vermelho", "verde", "azul")

print(cores[0])
print(cores[-1])

#Q8 ---- Por que tupla é imutavel

cores = ("vermelho", "verde", "azul")
cores2 = ("amarelo", "roxo")

print(cores + cores2)

cores = ("vermelho", "verde", "azul")
cor1,cor2,cor3 = cores
print(cor1)
print(cor2)
print(cor3)