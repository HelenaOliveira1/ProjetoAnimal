class Animal():
    def __init__(self, nome, numMembros, habitat):
        self.nome = nome
        self.numMembros = numMembros
        self.habitat = habitat

    def mover(self):
        print("%s está movendo de forma genérica."%self.nome)

    def comer(self):
        print("%s está comendo de forma genérica."%self.nome)

    def __str__(self):
        return ("Nome: %s\n Número de Membros: %i\n Habitat: %s\n"%(self.nome, self.numMembros, self.habitat))

    def __add__(self, other):
        return (self.numMembros + other.numMembros)
