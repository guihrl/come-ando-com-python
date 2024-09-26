primeiro_numero = 11 # snake case
Segundo_Numero = 12 # camel case
terceiroNumero = 13 # pascal case

print ("hello word") #Ele vai colocar no terminal o que você quer que ele fale

#iniciando declaracao de variaveis
nome = "guilherme" #String = sequência de caracteres alfanuméricos, como letras, números e símbolos
idade = 17         #Inteiro = números inteiros
altura = 1.79      #Float = ponto flutuante

#numeros
x = 10 #tipo inteiro
y = 3.14 #tipo float
z = 1 + 2j #operação matemática

#Sequência
string = "Olá, mundo"
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

#Mapping
dicionario = {'nome': 'Guilherme', 'idade': '17', 'cidade': 'Recife'}

#Boleanos
verdadeiro = True
falso = False

#Outros
nulo= None
tipo_objeto = type('colocar o nome de uma variável aqui!')


#criando um exemplo de variaveis
salarioBase = float(input("Salario Base: "))
gratificacao = float(input("Gratificação: "))

#Processamento
salarioBruto = salarioBase + gratificacao

#saida
print ("O valor de salário bruto é R$",salarioBruto)

#desafio 01
nomeHotel = input("qual é o nome do hotel? : ")
estrelasHotel = float(input("Qual é a quantidade de estrelas que o hotel tem? : "))
cidadeHotel = input("Em que cidade fica?: ")

# if estrelasHotel >= 6:
#     print("coloque um número de 1 a 5")
# else:
print(f"**********************\n*********{nomeHotel}*********\n*****{estrelasHotel} estrelas*****\n********{cidadeHotel}********\n**********************")

# **********************
# *********Ibis*********
# *****5.0 estrelas*****
# ********Recife********
# **********************

# Operadores relacionais

# == - Igual a
# != - Diferente de
# > - maior que
# >= - maior igual
# < - menor que
# <= - menor igual

x = 10
y = 5

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

# Operadores Lógicos
#E(or)
# O (or) só precisa um dos dois números sejam verdadeiros para ser True
#ou(and)
# O and precisa que os dois números sejam verdadeiros para ser True

#Desvios Condicionais
#if
#elif
#else

#Exemplo

cupom = input("Digite o cupom: ")

if (cupom=="FUCTURA1" or cupom=="FUCTURA2"):
    print("Você ganhou 15% de desconto")

#Exemplo ultilizando IF e ELSE

cupom = input("Digite o cupom: ")

if (cupom=="FUCTURA1" or cupom=="FUCTURA2"):
    print("Você ganhou 15% de desconto")
else:
    print("Você ganhou 10% de desconto")

#Exemplo ultilizando IF, ELSE e ELIF

cupom = input("Digite o cupom: ")

if (cupom=="FUCTURA1"):
    print("Você ganhou 15% de desconto")
elif(cupom=="FUCTURA2"):
    print("Você ganhou 10% de desconto")
elif(cupom=="FUCTURA1" and cupom=="FUCTURA2"):
    print("Você ganhou 50% de desconto")
else:
    print("Você ganhou 5% de desconto")

#Operação e Operador
# Adição       +
#Subitração    -
#Multiplicação *
# Divisão      /
#

#Desafio 2

emptrestimo = float(input("Digite o emprestimo que você que pegar do banco: "))
salario = float(input("Digite o seu salario: "))

if (emptrestimo <=  salario*0.5):
    print ("O emptrestimo será aprovado!!")
elif (emptrestimo <= salario*0.75):
    print("A situação ficará em análise")
else:
    print("Seu emprestimo não foi aprovado")



x = float(input("digite um número: "))
resolucao = x/2

if( resolucao %2 ==0):
    print(f"{resolucao}é par")
else:
    print(f"{resolucao}é impar")

#Estrutura de dados

#Lista = []
minha_lista = [1, 2, 3, "quatro", True]#VÁ EM listas.py PRA VER EXERCICIOS
