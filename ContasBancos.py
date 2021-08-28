from datetime import datetime
import pytz #modulo que faz ajuste de fuso horario automaticamente
from random import randint #bilioteca que gera numeros aleatórios

class ContaCorrente():
    """
        Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

        Atributos:
            nome (str): Nome do Cliente
            cpf (str): CPF do Cliente. Deve ser inserido com pontos e traços
            saldo: Saldo disponivel na conta do cliente
            limite: Limite de cheque especial daquele cliente
            agencia: Agencia responsável pela conta do cliente
            nun_conta: Numero da conta corrente do cliente
            transações: Histórico de transações do cliente
    """

    #metodo estatico que não depende de nada em nossa classe, mas que será utilizado para pegar data e hora
    #uma função auxiliar dentro da classe. Também será um metodo não publico por isso começa com _
    @staticmethod #sinalização que é um metodo estatico
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East') #utilizar os modulos de data e fuso - esse é o horario de brasilia
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S') #strftime é um metodo para formatar datas

    #criando parametros obrigatorios
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome #o _ significa que não quero que ninguém mexa
        self.cpf = cpf
        self._saldo = 0 #parametro não obrigatorio
        self._limite = None #criado parametro para utizar no limite_conta
        self.agencia = agencia
        self.num_conta = num_conta
        self._transacoes = []
        self.cartoes = [] #inserido esse atributo para que possamos associar o cartão a conta corrente

    def consultar_saldo(self):
        """
            Esse metodo foi construído para utilizar o atributo saldo. Saldo não pode ser modificado ou consultadi diretamente.
            Por isso foram construídos esses metodos.
            Exibe o saldo atual da conta do cliente.
            Não há parametros necessários.
        """
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        """
             Esse metodo foi construído para utilizar o atributo saldo. Saldo não pode ser modificado ou consultadi diretamente.
             Por isso foram construídos esses metodos.
        """
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

# 2) CRIAR UM METODO PARA SER USADO/CONSUMIDO EM OUTRAS REGRAS
# quando coloca o "_" é um metodo privado que não é para ser modificado
    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        """
            Esse metodo foi construído para utilizar o atributo saldo. Saldo não pode ser modificado ou consultadi diretamente.
            Por isso foram construídos esses metodos.
        """
# 1) CRIAR REGRA NO METODO PARA VERIFICAR SE PODE OU NÃO SACAR DINHEIRO
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
    #Caso contrário do if pode sacar o dinheiro
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print('Seu limite de cheque Especial é de R${:,.2f}'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print (transacao)

    def trasnferir(self, valor, conta_destino): #conta_destino será um objeto com os mesmos atributos da classe
        """
             Esse metodo foi construído para utilizar o atributo saldo. Saldo não pode ser modificado ou consultadi diretamente.
             Por isso foram construídos esses metodos.
        """
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, self._saldo, ContaCorrente._data_hora())) #transacao é o historico


class CartaoCredito():

    @staticmethod  # sinalização que é um metodo estatico
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')  # utilizar os modulos de data e fuso -
        # esse é o horario de brasilia
        horario_BR = datetime.now(fuso_BR)
        return horario_BR  # não precisa ser formatado, só a data mesmo

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9)) #macete para gerar 3 numeros
        # aleatorios. Utiliza isso para poder iniciar com 0
        self.limite = 1000 # se precisar cria-se um novo metodo para dar um limite para ele
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property #torna o atributo _senha uma propriedade - get
    def senha(self): #definição do metodo em que force o usuário a colocar 4 numeros
        # criar metodo get e metodo set para ter uma validação nesse campo
        #logica
        return  self._senha

    @senha.setter #sempre que precisar validar o atributo definir esses 2 metodos - set
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric(): #se valor tem 4 numeros e é numerico
            self._senha = valor # se for vou modificar a senha
        else: # caso contrário
            print("Nova senha inválida")


