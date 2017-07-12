from Cachorro import Cachorro
from Galinha import Galinha
from Animal import Animal

def main():

    a1 = Animal("Susy", 4, "matas")

    c1 = Cachorro("preto", "Dog", 4, "doméstico")
    c1.mover()
    c1.farejar()

    g1 = Galinha("Zefa", 2, "granja")
    g1.mover()
    g1.ciscar()

    print("Animal:\n " + str(a1) + "Cachorro:\n " + str(c1) + "Galinha:\n " + str(g1))

    r1 = c1+g1
    print("Soma do número de membros: ", r1)

if (__name__ == "__main__"):
    main()
