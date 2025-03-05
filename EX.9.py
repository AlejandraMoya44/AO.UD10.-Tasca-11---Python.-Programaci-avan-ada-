"""
Crear una llista dels 10 primers números elevats a una potència donada. Utilitzar list comprehensions. 
Ex: Si volem el quadrat dels números de la llista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , retorni [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], si la volem del cub retorni [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] i així successivament.
"""
def llista_potencies(n, pot):
    return [x ** pot for x in range(n + 1)]

n = 10
potencia = 2
resultat = llista_potencies(n, potencia)
print(resultat)

"""
Crear una llista dels 10 primers números elevats a una potència donada. Utilitzar list comprehensions. 
Ex: Si volem el quadrat dels números de la llista [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] , retorni [0, 1, 4, 9, 16, 25, 36, 49, 64, 81], si la volem del cub retorni [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] i així successivament.
"""
def llista_potencies(n, pot):
    return [x ** pot for x in range(n + 1)]

n = 10
potencia = 3
resultat = llista_potencies(n, potencia)
print(resultat)