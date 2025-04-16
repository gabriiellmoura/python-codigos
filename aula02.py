class Carro:
    def __init__(self, nome_carro):
        #self.nome = 'Porsche 911 Turbo'
        #self.nome1 = 'Porsche Macan 4 (2025)'  #hard coded
        self.nome_carro = nome_carro
    
    def acelerar(self):
        print(f'{self.nome_carro} estar acelerando')

porsche1 = Carro('Porsche 911 Turbo')
#porsche1 = Carro(100, 300)
porsche1.acelerar()
print(porsche1.nome_carro)


porsche2 = Carro('Macan 4 (2025)')
print(porsche2.nome_carro)

porsche3 = Carro('Macan (2025)')
print(porsche3.nome_carro)