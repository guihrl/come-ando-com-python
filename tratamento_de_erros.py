# resultado = 10/0
# print(resultado)

#exemplo
# try:
#     resultado = 10/0

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida")
    
#exemplo
# try:
#     resultado = 10/2

# except ZeroDivisionError:
#     print("Erro: Divisão por zero não é permitida")
# else:
#     print(f"O resultado é {resultado}")

#exemplo

# try:
#     arquivo = open('dados.txt', 'r')
#     conteudo = arquivo.read
# except FileNotFoundError:
#     print("Erro: Arquivo não encontrado.")
# finally:
#     print("Operação finalizada.")

#exemplo

# def verificar_idade(idade):
#     if idade < 18:
#         raise ValueError("Idade deve ser maior ou igual a 18")
#     else:
#         print("entrada permitida")

# try:
#     verificar_idade(18)
# except:

# class SaldoInsuficienteError(Exception):
#     """Exeção levantada quando o saldo é insuficiente para realizar uma transação"""
#     pass

# def sacar(valor, saldo):
#     if valor > saldo:
#         raise SaldoInsuficienteError("Saldo insuficiente para sacar o valor solicitado.")
#     saldo-=valor
#     return saldo

# try:
#     saldo_atual = sacar(1500, 1000)
# except SaldoInsuficienteError as e:
#     print(e)
    
# class MenorDeIdadeError(Exception):
#     pass

# def numero(idade):
#     if idade < 18:
#         raise MenorDeIdadeError("Ei moçinho você é menor de idade. Vá embora daqui.")
#     idade = 15
#     return idade

# try:
#     idade_atual = numero(15)
# except MenorDeIdadeError as Menor:
#     print(Menor)

class OIndiceError(Exception):
    pass
    
lista = [1, 2, 3,6 ,4]

def criar_lista():
    for i,item in enumerate(lista):
        print(f"{i}:{list}")
    
try:
    indice = int(input("Digite o índice da lista que você deseja acessar: "))
    
    if 0 <= indice < len(lista):
        print(f"O valor no índice {indice} é: {lista[indice]}")
    
except OIndiceError:
    print("Você colocou o indice errado tente, novamente.")