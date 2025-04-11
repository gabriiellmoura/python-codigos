class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Enderecos(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('apagando...', self.nome)

class Enderecos:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('apagando...', self.rua, self.numero)

cliente01 = Cliente('Maria')
cliente01.inserir_enderecos('Av Castelo Branco', 56)
cliente01.inserir_enderecos('Av Rui Barbosa', 782)
cliente01.listar_enderecos()
del cliente01
#print(cliente01.enderecos[1].rua)