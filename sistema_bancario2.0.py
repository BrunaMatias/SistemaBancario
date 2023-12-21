#menu para gerenciar todos usuarios:
menu_geral = """
    ==== Menu Geral ====
    [u] Cadastrar usuário
    [c] Criar conta
    [m] Menu do usário
    [q] Encerrar
>= """

#menu para movimentações individuais:
menu_usuario = """    
    === Menu Individual ===
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [v] Voltar para menu geral
>= """

extrato_header = """ 
            Extrato        
--------------------------------
Operação:               Valor:
"""

extrato_tail = """
--------------------------------
"""

usuarios = list()  #lista com todos usuários cadastrados
contas_ativas = 0

#função de depósito:
def deposito(indice, valor):
    if "saldo" not in indice: #adiciona chaves caso não existam
        indice["saldo"] = 0  
    if "historico_deposito" not in indice:
        indice["historico_deposito"] = list() 
    
    indice["historico_deposito"].append(valor) #adiciona valor depositado ao histórico
    indice["saldo"] += valor

    print(f"R${valor} depositado com sucesso")
    return indice["saldo"]

#função de saque:
def saque(indice, valor):
    if "saldo" not in indice: #adiciona chaves caso não existam
        indice["saldo"] = 0  
    if "historico_saque" not in indice:
        indice["historico_saque"] = list() 
    
    if valor > indice["saldo"]:
        print("Saldo insuficiente")
    else:
        indice["saldo"] -= valor
        indice["historico_saque"].append(valor) #adiciona valor sacado ao histórico
        print(f"R${valor} sacado com sucesso")

    return indice["saldo"]

#função de extrato:
def extrato(indice):
    if "saldo" not in indice: #adiciona chaves caso não existam
        indice["saldo"] = 0  
    if "historico_saque" not in indice:
        indice["historico_saque"] = list() 

    elif len(indice["historico_deposito"]) > 0 or len(indice["historico_saque"] > 0): 
        for i in indice["historico_deposito"]:
            print(f"Deposito:               R${i} ") #imprime depositos

        for i in indice["historico_saque"]:
            print(f"Saque:                  R${i} ") #imprime saques

    return indice["saldo"]

while True:
    opcao = input(menu_geral)

    #operação de cadastro de usuário:
    if opcao in "Uu":   
        pessoa = dict() #protótipo pessoa = {cpf, "nome", data_nascimento, "endereco", agencia, conta, saldo, historico_deposito(), historico_saque()}

        print("\nCadastro de usuário")
        pessoa["cpf"] = int(input("informe o CPF: "))

        existe = any(i["cpf"] == pessoa["cpf"] for i in usuarios)

        if existe:
            print("Usuário com esse CPF já cadastrado")
        else:
            pessoa["nome"] = str(input("Informe o nome: "))
            pessoa["data_nascimento"] = int(input("Informe a data de nascimento: "))
            pessoa["endereco"] = str(input("informe o endereço: "))
            usuarios.append(pessoa.copy()) #adiciona pessoa a lista com todos usuários

    #operação de cadastro de conta corrente:
    elif opcao in "Cc":  
        cpf = int(input("Informe o cpf do usuário: "))

        for i in usuarios:     #procura cpf na lista de usuários cadastrados
            if i["cpf"] == cpf:  
                i["agencia"] = 1000         
                i["conta"] = contas_ativas + 1
                i["saldo"] = 0
                contas_ativas += 1
                print(f"Conta criada com sucesso! Nome: {i['nome']}, n° conta: {i['conta']}, agência: {i['agencia']}")
                break
        else:
            print("CPF não encontrado, primeiro cadastre o usuário")

    #menu de operações do usuário:
    elif opcao in "Mm":

        if len(usuarios) > 0:

            cpf_usuario = int(input("Informe o CPF da usuário: "))
            indice_usuario = None 
      
            for i in usuarios: #busca índice da lista de usuarios associado ao cpf informado
                if i["cpf"] == cpf_usuario:
                    existe_cpf = True
                    indice_usuario = i  

                    if existe_cpf: 
                        if "conta" not in i: 
                            print("Usuário sem conta ativa, crie uma conta primeiro")

                        else:
                            while True: 
                                opcao_usuario = input(menu_usuario) 

                                if opcao_usuario in "Dd": #operação de deposito
                                    valor_deposito = float(input("Informe o valor a ser depositado: "))
                                    deposito(indice_usuario, valor_deposito)

                                elif opcao_usuario in "Ss": #operação de saque
                                    valor_saque = float(input("informe o valor do saque: "))
                                    saque(indice_usuario, valor_saque)

                                elif opcao_usuario in "Ee": #operação de extrato
                                    print(extrato_header)
                                    extrato(indice_usuario)
                                    print(f"\nSaldo:                  R${indice_usuario['saldo']}")   
                                    print(extrato_tail)

                                    print(f"""Nome: {indice_usuario['nome']}
Data nascimento : {indice_usuario['data_nascimento']}
Conta: {indice_usuario['conta']}
Agência: {indice_usuario['agencia']}""")
                                    
                                elif opcao_usuario in "Vv": #operação de encerrar menu do usuário
                                    print("Muito obrigado! Operação individual encerrada")
                                    break

                    else:
                        print("Nenhum usuário com esse CPF cadastrado")
                        break

        else: 
            print("Erro, nenhum usuário cadastrado")

    #operação de encerrar programa:        
    elif opcao in "Qq": 
        print("Muito obrigado(a), Programa encerrado!")
        break