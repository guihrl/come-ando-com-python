# Crie um programa que permita ao usuário realizar as seguintes operações bancárias:

# Criar conta
# Verificar saldo
# Depositar dinheiro
# Sacar dinheiro
# Encerrar o atendimento

# O programa deve armazenar as informações da conta bancária do usuário em um dicionário.
# O programa deve exibir um menu para o usuário escolher a operação que deseja realizar e, em seguida, executar a operação escolhida.
# Ao depositar dinheiro, o programa deve atualizar o saldo da conta bancária adicionando o valor depositado ao saldo atual.
# Ao sacar dinheiro, o programa deve verificar se o valor a ser sacado é menor ou igual ao saldo atual da conta bancária e, em caso afirmativo, atualizar o saldo da conta bancária subtraindo o valor sacado do saldo atual.
# Se o valor a ser sacado for maior que o saldo atual da conta bancária, o programa deve exibir uma mensagem informando que não há saldo suficiente na conta bancária para realizar a operação.


dic_informacao = {}
saldo = {20000}

while True:
    def criar_conta():
        nome = input("Nome e Sobrenome: ")
        senha = input("Crie sua senha(A senha tem que ter 4 digitos): ")
        dic_informacao[nome] = senha
        print(f"Muito obrigado, sr(a) {nome} por criar a sua conta.")
        print(f"Sua senha é {senha}, não compartilhe com ninguém")

        return nome, senha

    def verificar_saldo(saldo):
            print(f"seu saldo é de {saldo}")

    def depositar_saldo():
        adcSaldo = float(input("Digite quanto você quer depositar: "))
        saldoTotal = adcSaldo + saldo
        print(f"Seu saldo foi atualizado para {saldoTotal} ")
        return saldoTotal

    def sacar_dinheiro():
        
        sacar = float(input("Quanto você quer sacar:  "))
        
        global saldo
        if sacar > saldo:
                print(f"Erro. Seu saque maximo é de R$ {saldo}")
        else:
            saldo -= sacar
            print(f"Saque feito com sucesso!! Agora você está com R$ {saldo} ")

        return saldo     

    print("1 - Criar Conta")
    print("2 - Verificar Saldo")
    print("3 - Depoditar Saldo")
    print("4 - Sacar Dinheiro")
    print("5 - Encerrar o Atendimento")

    escolha = input("Digite um número da sua escolha: ")

    if escolha == "1":
        criar_conta()

    elif escolha == "2":
        verificar_saldo('saldo')

    elif escolha == "3":
        
        depositar_saldo(saldo)
    
    elif escolha == "4":
        sacar_dinheiro()
    
    else:
        escolha = "5"
        break
    
    
#--------------------------------------------------------------------------------------------------------------
# Problema: Dado um conjunto de notas de alunos, calcule a média e classifique como "Aprovado" ou "Reprovado" (nota mínima 7).


