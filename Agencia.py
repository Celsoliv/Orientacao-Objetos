from random import randint #gerador de numero aleatorio

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'.format(self.caixa))
        else:
            print('O Valor do caixa está ok. Caixa Atual:{}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponivel em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

#AgenciaVirtual que será filha da classe Agencia.
class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000) #usar o metodo init da classe Agencia, 1000 será o numero padrão para agencia virtual
        self.caixa = 1000000 #significa que obrigatoriamente ela vai ter que ter 1.000.000 quando for criada
        self.caixa_paypal = 0 #será utilizado apenas para metodo na classe AgenciaVirtual

    def depositar_paypal(self, valor):
        self.caixa -= valor #tirei o valor do caixa - aqui poderiamos colocar os IF´s para verificar se tem o valor ou não
        self.caixa_paypal += valor #coloquei o valor no paypal

    def secar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


#AgenciaComum
class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj): #pegando as informações da super classe Agencia sem o numero
        super().__init__(telefone, cnpj, numero=randint(1001, 9999)) #colando um numero aleatorio no atributo numero
        self.caixa = 1000000


#AgenciaPremium
class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj): #pegando as informações da super classe Agencia sem o numero
        super().__init__(telefone, cnpj, numero=randint(1001, 9999)) #colando um numero aleatorio no atributo numero
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            #adicionar cliente utilizando a super classe
            super().adicionar_cliente(nome, cpf, patrimonio)

        else:
            print ('O Cliente não tem patrimônio minimo necessário para entrar na Agência Premium')


if __name__ == '__main__': #para não rodar esses programas no arquivo main que está utilizando as classes
    agencia1 = Agencia(22223333, 2000000000, 5281)

    agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 2433252, 10001000002)
    agencia_virtual.verificar_caixa()
    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    print('-' * 20)

    agencia_comum = AgenciaComum(43445050, 3345439543)
    agencia_comum.verificar_caixa()

    print('-' * 20)
    agencia_premium = AgenciaPremium(33334444, 1000000001)
    agencia_premium.verificar_caixa()

    agencia_premium.adicionar_cliente('Cliente_premium', 5324994358, 50000000)
    print(agencia_premium.clientes)

    print('-' * 20)
    print('-' * 20)
    agencia1.caixa = 100

    agencia1.verificar_caixa()
    agencia1.emprestar_dinheiro(1500, 32194454324, 0.02)
    agencia1.adicionar_cliente('Celso', 12344566030, 10000)
    print(agencia1.clientes)
