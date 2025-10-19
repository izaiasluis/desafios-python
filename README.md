# desafios-python
Soluções para os desafios da trilha de Python da DIO, Bootcamp Luizalabs

1º Sistema Bancário - Desafio 1

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
