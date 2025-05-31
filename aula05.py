class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
            return Pessoa.ano_atual - self.idade

dados = {'nome': 'jose gabriel', 'idade': 23}
p1 = Pessoa(**dados)
'''
p2 = Pessoa('helena', 12)

p1.__dict__['nome'] = 'jose gabriel' # dict não é somente para leitura.

print(p1.ano_nascimento())
print(p2.ano_nascimento())
'''
#print(p1.nome)
print(vars(p1))