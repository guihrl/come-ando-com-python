dic_informacao = {}
saldo = 20000

while True:
    def criar_conta():
        nome = input("Nome e Sobrenome: ")
        senha = input("Crie sua senha(A senha tem que ter 4 digitos): ")
        dic_informacao[nome] = senha
        print(f"Muito obrigado, sr(a) {nome} por criar a sua conta.")
        print(f"Sua senha é {senha}, não compartilhe com ninguém")

        return nome, senha

    def verificar_saldo():
        
        print(f"seu saldo é de {saldo}")
        
    
    def depositar_saldo(saldo):
        adcSaldo = float(input("Digite quanto você quer depositar: "))
        saldoTotal = adcSaldo + saldo
        print(f"Seu saldo foi atualizado para {saldoTotal} ")
    
        return saldoTotal

    def sacar_dinheiro():
        global saldo
        sacar = float(input("Quanto você quer sacar:  "))

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
        verificar_saldo(saldo)

    elif escolha == "3":
        
        depositar_saldo(saldo)
    
    elif escolha == "4":
        sacar_dinheiro()
            

