menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
>= """ 

saldo = 0
limite = 500
numero_saques = 0
historico_de_saques = []
LIMITE_SAQUES = 3
numero_de_depositos = 0
historico_de_depositos = []

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        
        valor_depositado = float(input("Informe a quantia a ser depositada:"))
        saldo += valor_depositado
        historico_de_depositos.append(valor_depositado)
        numero_de_depositos +1

    elif opcao == "s":
        print("Sacar")

        if numero_saques < LIMITE_SAQUES:
            valor_solicitado = float(input("Informe a quantia desejada para o saque:"))

            if(valor_solicitado <= saldo):
                saldo -= valor_solicitado
                historico_de_saques.append(valor_solicitado)
                print(f"Saque de R${valor_solicitado} efetuado com sucesso!")
                numero_saques += 1
            else:
                print("Saldo insuficiente")

        else: 
            print("Quantidade máxima de saques diários atingidos")
    
    elif opcao == "e":
        print("Extrato")

        print(""" 
            Extrato        
--------------------------------
Histórico:            Valor:
""")

        for deposito in historico_de_depositos:
            ###colocar lstrip
            print("Depósito:             R$", deposito)

        for saque in historico_de_saques: 
            print("Saque:                R$", saque)

        print(f"""
--------------------------------
Saldo atual:          R${saldo}
""")
    
    elif opcao == "q": 
        break

    else: 
        print("Operação inválida, por favor selecione novamente a opção desejada.")