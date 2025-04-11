class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.ano_modelo = None
        self._motor = None
        #self._fabricante = None

    @property
    def motor1(self):
        return self._motor
    
    @motor1.setter
    def motor1(self, valor):
        self._motor = valor

    @property
    def fabricante1(self):
        return self._fabricante
    
    @fabricante1.setter
    def fabricante1(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
 
#class Ano_modelo:
#    def __init__(self, nome):
#        self.nome = nome

mustang = Carro('mustang shelby gt500')
ford = Fabricante('Ford motor company')
motor = Motor('motor V8 5.2 Supercharged')
#modelo = Ano_modelo('2022')
mustang.fabricante = ford
mustang.motor = motor
#mustang.modelo = modelo
print(mustang.nome, mustang.fabricante.nome, mustang.motor.nome)