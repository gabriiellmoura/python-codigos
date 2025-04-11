import json

CAMINHO_ARQUIVO = 'arquivo01.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.iddade = idade

p1 = Pessoa('jose', 12)
p2 = Pessoa('augusto', 34)
p3 = Pessoa('maria', 21)
bd = [vars(p1), p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
