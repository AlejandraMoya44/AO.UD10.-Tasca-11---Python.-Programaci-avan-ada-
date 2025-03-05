"""
Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho.
"""
def dividir(a, b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        return "Error: No es pot dividir per zero."

a = 10
b = 2
resultat = dividir(a, b)
print(resultat)

"""
Crear una funció que controli la divisió per zero i ens avisi que volem fer-ho.
"""
def dividir(a, b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        return "Error: No es pot dividir per zero."

a = 10
b = 0
resultat = dividir(a, b)
print(resultat)