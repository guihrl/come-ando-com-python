dic_informacao = {}

while True:
    print("1 - Criar Conta")
    print("2 - Verificar Saldo")
    print("3 - Depoditar Saldo")
    print("4 - Sacar Dinheiro")
    print("4 - Encerrar o Atendimento")

    escolha = input("Digite um número da sua escolha: ")

    if escolha == "1":
        def criar_conta():
            nome = input("Nome e Sobrenome: ")
            senha = input("Crie sua senha(A senha tem que ter 4 digitos): ")
            dic_informacao[nome] = senha
            print(f"Muito obrigado, sr(a) {nome} por criar a sua conta.")
            print(f"Sua senha é {senha}, não compartilhe com ninguém")
            return nome, senha


    if escolha == "2":
        def verificar_saldo():
            saldo = 20000.00
            print(f"seu saldo é de {saldo}")
            return saldo
    verificar_saldo()
    if escolha == "3":
        def depositar_saldo(saldo):
            adcSaldo = float(input("Digite quanto você quer depositar: "))
            saldoTotal = adcSaldo + saldo
            print(f"Seu saldo foi atualizado para {saldoTotal} ")
            

