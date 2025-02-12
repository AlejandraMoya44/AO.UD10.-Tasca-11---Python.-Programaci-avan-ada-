"""
Crear una funció que donada una llista de dígits ordenats, retorni el número corresponent. 
Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. Ex: def Passar_a_Numero(llista): -- retorni el número que corresponen els dígits.
"""
from functools import reduce

def Passar_a_Numero(llista):
    return reduce(lambda x, y: x * 10 + y, llista)

digits = [3, 4, 1, 5]
resultat = Passar_a_Numero(digits)
print(resultat)