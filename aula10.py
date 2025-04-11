# Aula 214 - encapsulamento
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       Pode ser usado em qualquer lugar
# _ (um underline) = protected
#       Não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       Só DEVE ser usado na classe em que foi
#       declarado.
#from functools import partial
class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'
    
    def metodo_publico(self):
        #self._metodo_protected()
        #print(self._protected)
        print(self.__private)
        return 'metodo publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
'''
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
'''
f = Foo()
#print(f.public)
print(f.metodo_publico())