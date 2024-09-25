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