from Animal import Animal

class Cachorro(Animal):
    def __init__(self, corPelo, nome, numMembros, habitat):
        super(Cachorro, self).__init__(nome, numMembros, habitat)
        self.corPelo = corPelo

    def mover(self):
        print(self.nome + " está se movendo como cachorro.")

    def farejar(self):
        print(self.nome + " está farejando.")
