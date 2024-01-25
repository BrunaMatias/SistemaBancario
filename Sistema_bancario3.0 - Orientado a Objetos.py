# Definição dos menus
menu_principal = """
───────────── Menu Geral ─────────────
[u] Cadastrar novo usuário
[c] Criar nova conta
[m] Menu do usuário
[x] Encerrar programa
>= """

# Menu para movimentações individuais
menu_operacoes = """    
    ─────── Menu do Usuário ───────
    [+] Depositar
    [-] Sacar
    [=] Extrato
    [<] Voltar para Menu Geral
    >= """

# Mensagem para criar uma conta
menu_tipo_conta = """
    Selecione o tipo de conta:
    [1] Conta Comum
    [2] Conta Corrente
    >= """

# Menu para cadastro de usuarios
menu_cadastro_usuario = """    
    ────── Cadastro de usuário ─────
"""

# Menu para cadastro de contas
menu_cadastro_conta = """    
    ─────── Cadastro de conta ──────
"""

# Cabeçalho para o extrato
cabecalho_extrato = """ 
    ─────────── Extrato ───────────
    Operação:                Valor:
"""

# Listagem de contas disponíveis
menu_contas_disponiveis = """ 
    ────── Contas disponíveis ─────
    Número:                 Saldo:"""

# Rodapé
rodape = """
    ───────────────────────────────
"""

# Definição da classe Conta
class Conta:
    def __init__(self, cpf, nome, saldo, id_conta, agencia):
        self._nome = nome
        self._cpf = cpf
        self._saldo = saldo
        self._id_conta = id_conta
        self._agencia = agencia
        self._historico = []

    def consultar_saldo(self):
        print(f"    Saldo atual: R${self._saldo}")
    
    def depositar(self, valor):
        self._saldo += valor
        self._historico.append(("Depósito", valor))
        print(f"    Depósito de R${valor} realizado com sucesso")

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._historico.append(("Saque   ", valor))
            print(f"    Saque de R${valor} realizado com sucesso")
        else:
            print("    Saldo insuficiente")

    def info_extrato(self):
        return f"    Número da conta: {self._id_conta}\n    Proprietário: {self._nome}\n    Cpf: {self._cpf}"

# Definição da classe ContaCorrente, que herda da classe Conta
class ContaCorrente(Conta):
    LIMITE_VALOR_SAQUE = 5000.00 
    LIMITE_SAQUES = 3 
    total_saques = 0

    def sacar(self,valor):
        if valor <= self.LIMITE_VALOR_SAQUE:
            if self.total_saques < self.LIMITE_SAQUES:
                self.total_saques += 1
                return super().sacar(valor)
            else:
                print(f"    Saque não realizado, limite de 3 transaçãoes atingido")
        else:
            print(f"    Saque não realizado, limite de R${self.LIMITE_VALOR_SAQUE} atingido")
        
# Definição da classe Cliente
class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._endereco = endereco

        self._contas_associadas = list()

    def adicionar_conta(self, numero_total_contas):
        self._id_conta = numero_total_contas + 1

        opcao = int(input(menu_tipo_conta))

        if opcao == 1:
            nova_conta = Conta(self._cpf, self._nome, 0, self._id_conta, 1000)
            self._contas_associadas.append(nova_conta)
            contas_abertas.append(nova_conta) 
            print(f"    Conta Comum criada com sucesso!")

        elif opcao == 2:
            nova_conta = (ContaCorrente(self._cpf, self._nome, 0, self._id_conta, 1000))
            self._contas_associadas.append(nova_conta)
            contas_abertas.append(nova_conta)
            print(f"    Conta Corrente criada com sucesso!")
            
        else:
            print(f"    Opção inválida")

    def buscar_contas(self):
        if len(self._contas_associadas) > 0:

            print(menu_contas_disponiveis)
            for conta in self._contas_associadas:
                print(f"    {conta._id_conta}                       R${conta._saldo}")
            
            id_desejado = int(input(f"    info_extratorme o número da conta desejada: "))
            conta_encontrada = None

            for conta in contas_abertas:
                if conta._id_conta == id_desejado:
                    conta_encontrada = conta
                    break  

            if conta_encontrada:
                return conta_encontrada
            else:
                print(f"    Nenhuma conta com esse número encontrada")
                return None
        
        else:
            print(f"    Esse usuário não possui contas cadastradas")


# Lista de clientes cadastrados e contas abertas
clientes_cadastrados = list()
contas_abertas = list()
numero_total_contas = len(contas_abertas)

while True:
    opcao = input(menu_principal)

    # Cadastrar cliente
    if opcao in "Uu":
        print(menu_cadastro_usuario)
        cpf = int(input(f"    info_extratorme o CPF: "))
        cpf_disponivel = True
        
        for cliente in clientes_cadastrados:
            if cliente._cpf == cpf:
                cpf_disponivel = False
                print(f"    Usuário com CPF já cadastrado")
                break

        if cpf_disponivel:
            nome = input(f"    info_extratorme o nome: ")
            data_nascimento = input(f"    info_extratorme a data de nascimento: ")
            endereco = input(f"    info_extratorme o endereço: ")
            
            clientes_cadastrados.append(Cliente(cpf, nome, data_nascimento, endereco))
            print(f"    Usuário cadastrado com sucesso!")

    # Criar conta
    elif opcao in "Cc":
        print(menu_cadastro_conta)
        cpf_buscado = int(input(f"    info_extratorme o CPF do usuário: "))
        cliente_encontrado = None

        for cliente in clientes_cadastrados:
            if cliente._cpf == cpf_buscado:
                cliente_encontrado = True
                cliente_disponivel = cliente

        if cliente_encontrado:
            cliente_disponivel.adicionar_conta(numero_total_contas)
            numero_total_contas += 1
             
        else:
            print("Usuário não encontrado")

    # Menu do usuário
    elif opcao in "Mm":
        cpf_buscado = int(input("info_extratorme o CPF do usuário: "))
        cliente_atual = None

        for cliente in clientes_cadastrados:
            if cliente._cpf == cpf_buscado:
                cliente_atual = cliente

        if cliente_atual:
            conta_desejada = cliente_atual.buscar_contas()  

            if conta_desejada:
                while True:
                    opcao_usuario = input(menu_operacoes)

                    # Depositar
                    if opcao_usuario == "+":
                        valor_deposito = float(input(f"    info_extratorme o valor a ser depositado: "))
                        conta_desejada.depositar(valor_deposito)
                    
                    # Sacar
                    elif opcao_usuario == "-":
                        valor_saque = float(input(f"    info_extratorme o valor para o saque: "))
                        conta_desejada.sacar(valor_saque)
                    
                    # Extrato
                    elif opcao_usuario == "=":
                        historico = conta_desejada._historico
                        print(cabecalho_extrato)

                        for operacao, valor in historico:  
                            print(f"    {operacao.capitalize()}              R${valor}")
                        
                        print(rodape)
                        print(f"    Saldo:                R${conta_desejada._saldo}")
                        print(f"{conta_desejada.info_extrato()}")
                        

                    # Voltar para o menu geral
                    elif opcao_usuario == "<":
                        break

                    else:
                        print("Opção inválida")
        
        else:
                print("Usuário não encontrado")             
    
    # Encerrar programa
    elif opcao in "Xx":
        print("Programa encerrado, muito obrigada!")
        break