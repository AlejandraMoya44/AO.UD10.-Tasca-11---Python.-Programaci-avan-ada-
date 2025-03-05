"""
Crear una llista amb les lletres d’una paraula qualsevol. 
Utilitzar list comprehensions. Ex: “institut”, retorni [‘i’,’n’,’s’,’t’,’i’,’t’,’u’,’t’].
"""
def lletres_paraula(paraula):
    return [lletra for lletra in paraula]

paraula = "institut"
resultat = lletres_paraula(paraula)
print(resultat)