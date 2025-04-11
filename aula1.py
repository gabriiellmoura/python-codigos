# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
'''
string = 'gabriel'
print(string.upper())
print(isinstance(string, str))
'''
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


objeto1 = Pessoa('gabriel', 'moura')
objeto2 = Pessoa('maria', 'joaquina')

print(objeto1.nome)
print(objeto1.sobrenome)

print('\n')

print(objeto2.nome)
print(objeto2.sobrenome)