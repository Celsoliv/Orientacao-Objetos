# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV: #criar uma classe

    cor = 'preta' #atributo fixo criado para a classe TV

    def __init__(self, tamanho): #atributos, sempre inicia com __init__ / tamanho virou atributo para escolher
        self.ligada = False
        self.tamanho = tamanho #tamanho é uma variavel
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal): #metodo da minha classe TV, novo_canal é um parametro
        self.canal = novo_canal
        print('Canal alterado para {}'.format(novo_canal))



#programa
# para criar uma TV eu preciso passar os parametro que escolhi no __init__
tv_sala = TV(tamanho=55) #cria a tv da sala com a classe TV / Criando uma instancia da TV / recebendo todos os atributos
tv_quarto = TV(tamanho=50)

tv_sala.quarto = 'verde'
tv_sala.mudar_canal("Globo") #aqui coloca o novo_canal que é o parametro
tv_quarto.mudar_canal('Youtube')

print(tv_sala.canal)
print(tv_quarto.canal)
print(tv_sala.cor)