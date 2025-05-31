# Aula 214 - encapsulamento
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