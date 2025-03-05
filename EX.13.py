"""
Crear una classe anomenada Animal que tingui els següents atributs d’objecte: especie i edat i els següents mètodes: xerrar (abstracte), mourem (abstracte) i quisoc. 
Llavors, crearem diferents subclasses:  Cavall, Dofí, Abella, Humà, Centaure.... que hauran de redefinir aquestes mètodes. Crearem una nova subclasse d’Humà, anomenada Fiet. 
Llavors, crearem una subclasse Centaure que heredarà de Cavall i Humà. Finalment, tindrem una nova classe xou que no té cap relació amb els altres, però que té els mateixos mètodes que Animal implementats.
Abella crearà un nou mètode anomenat, picar. 
Humà tindrà un nou atribut d’objecte anomenat, nom.
Fiet tindrà un nou atribut d’objecte anomenat, pares (llista). I un nou mètode anomenat nompares que ens mostrarà el nom dels pares.
Amb això, crear un llista d’elements de cada tipus i un for (bucle) que cridi als mètodes iguals.
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        return f"Sóc un {self.especie} i tinc {self.edat} anys."

class Cavall(Animal):
    def xerrar(self):
        return "Hiii!"

    def mourem(self):
        return "Estic galopant."

class Dofí(Animal):
    def xerrar(self):
        return "Eeeeee!"

    def mourem(self):
        return "Estic nedant."

class Abella(Animal):
    def xerrar(self):
        return "Bzzzz!"

    def mourem(self):
        return "Estic volant."

    def picar(self):
        return "T'he picat!"

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        return "Hola!"

    def mourem(self):
        return "Estic caminant."

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        return f"Els meus pares són: {', '.join(self.pares)}"

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Cavall.__init__(self, especie, edat)
        Humà.__init__(self, especie, edat, nom)

    def xerrar(self):
        return "Hola i Hiii!"

    def mourem(self):
        return "Estic caminant i galopant."

class Xou:
    def xerrar(self):
        return "Hola, sóc Xou!"

    def mourem(self):
        return "Estic movent-me."

    def quisoc(self):
        return "Sóc un xou especial!"

elements = [
    Cavall("cavall", 5),
    Dofí("dofí", 8),
    Abella("abella", 1),
    Humà("humà", 30, "Joan"),
    Fiet("humà", 15, "Marc", ["Pere", "Maria"]),
    Centaure("centaure", 12, "Centaure Joan"),
    Xou()
]

for element in elements:
    print(element.quisoc())
    print(element.xerrar())
    print(element.mourem())
    if isinstance(element, Abella):
        print(element.picar())
    if isinstance(element, Fiet):
        print(element.nompares())
    print()