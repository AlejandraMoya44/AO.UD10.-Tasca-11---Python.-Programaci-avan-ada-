"""
Crear una funció que permeti llegir la informació d’un fitxer, però que controli que el fitxer existeix i que la seva obertura no doni cap problema. 
Fes-ho també utilitzant with. Si voleu podeu practicar el try, except afegint-ho a les funcions anteriors.
"""
def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as fitxer:
            contingut = fitxer.read()
            return contingut
    except FileNotFoundError:
        return "Error: El fitxer no existeix."
    except IOError:
        return "Error: No es pot obrir el fitxer."

nom_fitxer = 'exemple.txt'
resultat = llegir_fitxer(nom_fitxer)
print(resultat)