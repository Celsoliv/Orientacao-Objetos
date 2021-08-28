from ContasBancos import ContaCorrente, CartaoCredito #traz as instancias das classes ContasBancos... outra forma de utilizar
from Agencia import AgenciaComum, AgenciaPremium, AgenciaVirtual, Agencia

#programa
#2 Associação cartão de credito
conta_Celso = ContaCorrente("Celso", "111.222.333-44", "1234", "52961")
conta_Celso.consultar_saldo()

#depositando um dinheiro na conta
conta_Celso.depositar(10000)
conta_Celso.consultar_saldo()

#sacando dinheiro na conta
#conta_Celso.sacar_dinheiro(10500)

print('Saldo Final')
conta_Celso.consultar_saldo()
conta_Celso.consultar_limite_chequeespecial()

print('-' * 20)
conta_Celso.consultar_historico_transacoes()

print('-' * 20)
conta_Xpto = ContaCorrente("Xpto", "222.333.444-55", "1234", "52962") #criar a nova conta usando a classe
conta_Celso.trasnferir(1000, conta_Xpto)

conta_Celso.consultar_saldo()
conta_Xpto.consultar_saldo()

conta_Celso.consultar_historico_transacoes()
conta_Xpto.consultar_historico_transacoes()

#2 continuação cartão de credito
print('-' * 20)
cartao_Celso  = CartaoCredito('Celso', conta_Celso)
print(cartao_Celso.conta_corrente.num_conta)
print(conta_Celso.cartoes[0].titular, conta_Celso.num_conta, cartao_Celso.numero, cartao_Celso.validade, cartao_Celso.cod_seguranca)

#sobre a senha
print('-' * 20)
cartao_Celso.senha = '150'
print(cartao_Celso.senha)

print(conta_Celso.__dict__) #consultar todos os dados da instância conta_Celso dentro da Classe. Traz um dicionário

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