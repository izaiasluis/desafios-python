'''
Sistema Bancário - Desafio 1

O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.

Objetivos geral: 
1. Separar funções existentes de depósito, saque e extrato em funções específicas.
2. Criar duas novas funções para cadastrar clientes e contas bancárias.
3. Cada função terá uma regra na passagem de argumentos e retorno de valores.

Observações: 
a) A função saque deve receber os argumentos apenas por nome (Keyword-Only Arguments).
   - Sugestão de argumentos: saldo, valor, limite, numero_saques, limite_saques.
   - Sugestão de retorno: saldo e extrato.
b) A função depósito deve receber os argumentos apenas por posição (Positional-Only Arguments).
   - Sugestão de argumentos: saldo, valor, extrato.
   - Sugestão de retorno: saldo e extrato.
c) A função extrato deve receber os argumentos tanto por posição quanto por nome (Positional-or-Keyword Arguments).
   - Sugestão de argumentos posicionais: saldo.
   - Sugestão de argumentos nomeados: extrato.
d) Criar usuário(cliente) - Deve armazenar (em lista) nome, data de nascimento, cpf, endereço. O endereço é uma string com o formato "logradouro, nro - bairro - cidade/sigla estado". Não podemos cadastrar dois clientes com o mesmo cpf. 
e) Criar conta corrente - Deve armazenar (em lista) o cliente e uma agência. O número da conta deve ser gerado sequencialmente começando em 1. Cada cliente pode ter mais de uma conta corrente. Porém uma conta só pode existir vinculada a um usuário. Número da agência é fixo (0001). 
Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.
'''
# ----------------------------------------------(variáveis globais)--------------------------------------------
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

AGENCIA = "0001"
clientes = []
contas = []
numero_conta_sequencial = 1

# -------------------------------------------(Funções de Movimentação)-----------------------------------------
def depositar(saldo, valor, extrato, /):
    """
    Realiza a operação de depósito na conta.

    Args:
        saldo (float): Saldo atual da conta. (Positional-Only /)
        valor (float): Valor a ser depositado. (Positional-Only /)
        extrato (str): Histórico de movimentações. (Positional-Only /)

    Returns:
        tuple: (Novo saldo, Novo extrato)
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque na conta, com validações de saldo, limite e saques.

    Args:
        saldo (float): Saldo atual da conta. (*Keyword-Only)
        valor (float): Valor a ser sacado. (*Keyword-Only)
        limite (float): Limite máximo de saque por operação. (*Keyword-Only)
        numero_saques (int): Contador de saques realizados. (*Keyword-Only)
        limite_saques (int): Limite máximo de saques diários. (*Keyword-Only)

    Returns:
        tuple: (Novo saldo, Extrato do movimento, Novo número de saques)
    """
    extrato_movimento = ""
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato_movimento = f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato_movimento, numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato_movimento, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato formatado e o saldo atual da conta.

    Args:
        saldo (float): Saldo atual da conta. (Positional-Only /)
        extrato (str): Histórico de movimentações. (*Keyword-Only)

    Returns:
        None: A função apenas imprime o extrato na tela.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# --------------------------------------------(Funções de Cadastro)-------------------------------------------------
# FUNÇÃO AUXILIAR
def filtrar_cliente(cpf, clientes):
    """
    Busca um cliente na lista pelo CPF.

    Args:
        cpf (str): O CPF do cliente a ser buscado.
        clientes (list): Lista de dicionários contendo os clientes cadastrados.

    Returns:
        dict or None: O dicionário do cliente se encontrado, ou None.
    """
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return cliente
    return None

# FUNÇÃO PRINCIPAL de CADASTRO DE USUÁRIO
def cadastrar_usuario(clientes):
    """
    Cadastra um novo usuário no sistema.

    Args:
        clientes (list): Lista de dicionários onde o novo cliente será adicionado.

    Returns:
        None: A função modifica a lista 'clientes' diretamente.
    """
    cpf = input("Informe o CPF (somente números): ")
    cliente_existe = filtrar_cliente(cpf, clientes)

    if cliente_existe:
        print("Já existe um cliente cadastrado com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

# FUNÇÃO PRINCIPAL de CADASTRO DE CONTA
def cadastrar_conta(agencia, numero_conta, clientes, contas):
    """
    Cria uma nova conta corrente e a vincula a um cliente existente.

    Args:
        agencia (str): Número da agência (Constante).
        numero_conta (int): Próximo número sequencial da conta.
        clientes (list): Lista de clientes cadastrados (para busca do CPF).
        contas (list): Lista de contas para adicionar a nova conta.

    Returns:
        int: O próximo número de conta sequencial (incrementado em caso de sucesso ou inalterado).
    """
    cpf = input("Informe o CPF do cliente para vincular à conta: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        conta = {
            'agencia': agencia,
            'numero_conta': numero_conta,
            'cliente': cliente
        }
        contas.append(conta)
        print(f'Conta {agencia} - {numero_conta} criada com sucesso!')
        return numero_conta + 1
    else:
        print("Cliente não encontrado. Conta não criada.")
        return numero_conta

def listar_contas(contas):
    """
    Exibe todas as contas cadastradas, mostrando a agência, número da conta, 
    e o nome/CPF do cliente vinculado.

    Args:
        contas (list): Lista de dicionários contendo as contas.

    Returns:
        None: A função apenas imprime as informações na tela.
    """
    print("\n=== Contas Cadastradas ===")
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for indice, conta in enumerate(contas, start=1):
        cliente = conta['cliente']

        print(f"""
              Conta:\t{indice}: 
              Agência:\t{conta['agencia']}, 
              Número:\t{conta['numero_conta']}, 
              Titular:\t {cliente['nome']}, 
              CPF:\t{cliente['cpf']}""")
# -------------------------------------------(Sistema Bancário)--------------------------------------------------
menu = """
================= MENU =================
      Escolha a operação desejada:
---------  --Movimentações--  --------
[d] Depositar
[s] Sacar
[e] Extrato
-----------  --Cadastros- ------------
[1] Cadastrar Usuário
[2] Cadastrar Conta
[3] Listar Contas
-------------  --Outros-- -----------
[q] Sair


=> """

while True:

    opcao = input(menu)

    if opcao == "d":    
        try:  
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        except ValueError:
            print("Operação falhou! O valor informado é inválido.")
            continue
                
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            saldo_novo, extrato_movimento, saques_feitos = sacar(saldo=saldo, valor=valor, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            saldo = saldo_novo
            extrato += extrato_movimento
            numero_saques = saques_feitos

        except ValueError:
            print("Operação falhou! O valor informado é inválido.")
            continue

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "1": # Novo Usuário
        cadastrar_usuario(clientes)

    elif opcao == "2": # Nova Conta
        numero_conta_sequencial = cadastrar_conta(
            AGENCIA, 
            numero_conta_sequencial, 
            clientes, 
            contas
        )
        
    elif opcao == "3": # Listar Contas
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        