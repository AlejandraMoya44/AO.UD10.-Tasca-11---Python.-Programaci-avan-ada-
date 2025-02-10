"""
Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem. 
Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.
"""
import string
from functools import reduce

def lenp(frase):
    paraules = frase.translate(str.maketrans("","", string.punctuation)).split()
    longituds = list(map(len, paraules))
    return longituds

frase = "Hola a tothom, com estem avui?"
resultat = lenp(frase)
print(resultat)

l = [-1, 0, 25, 3, -2, 4]

positius = list(filter(lambda a: a > 0, l))
print(positius)

parells = list(filter(lambda a: a % 2 == 0, l))
print(parells)

suma = reduce(lambda n1, n2: n1 + n2, l)
print(suma)

paraules = ["hola", "casa", "metge", "cadira"]

ordenat = sorted(paraules, key=lambda x: x.count('a'), reverse=True)
print(ordenat)