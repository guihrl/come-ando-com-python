#É uma sequencuia de caracteres que podem ser ultilizada para texto em python

#Declarando uma String

# mensagem = "Hello, Word"
# print(mensagem)

#Concatenando uma String

# primeiroNome = "João"
# print(primeiroNome)

# sobrenome = "Silva"
# print(sobrenome)

# nomeCompleto = primeiroNome + " " + sobrenome
# print(nomeCompleto)

#Acessando caracteres individuais em uma string

# primeiro_caractere = mensagem[0]
# segundo_caractere = mensagem[-1]
# print(primeiro_caractere)
# print(segundo_caractere)

# #encontrando o comprimento de uma string
# comprimento = len(mensagem)
# print(comprimento)

# #Convertendo uma string para letras maiúsculas ou minisnúscula
# caractere = mensagem[2:]
# maiuscula = mensagem.upper()
# minuscula = mensagem.lower()
# E = mensagem[1]
# H = mensagem[0]
# letraE = E.upper()
# letraH = H.lower()
# print(maiuscula)
# print(minuscula)

# juncao = letraH+ letraE + caractere

# print(juncao)

#split Divide uma string em substring com base em um delimitador

# palavras = mensagem.split(",")
# print(palavras)

# #in Verifica se uma substring está presente em uma string

# if "Word" in mensagem:
#     print("A substring 'word' está presente na mensagem.")

# #Substituindo caracteres em uma string

# nova_mensagem = mensagem.replace("Word" , "Python")
# print(nova_mensagem)

# #strip Remove espaços em branco de uma string

# frase = "  Hello, Word!  "
# sem_espacos = frase.strip() #retorna "Hello, Word"
# print(sem_espacos)

#"  " in texto

frase = "Estruturas de Dados em Python"
maiuscula = frase.upper()
print(frase)
print(maiuscula)

encontrar = frase.find('Dados')
print(encontrar)

nova_frase = frase.replace("Python", "Java")
print(nova_frase)

dividirEmListas = frase.split(" ")
print(dividirEmListas)