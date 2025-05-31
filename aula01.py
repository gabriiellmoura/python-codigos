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