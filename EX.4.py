"""
Crear una funció que donades dues llistes, les concateni amb un connector. Utilitzar zip. 
Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni [‘sub-campió’][‘supra-campiona’].
"""
def concatena_llistes(primera_llista, segona_llista, connector):
    return [a + connector + b for a, b in zip(primera_llista, segona_llista)]

primera_llista = ['sub', 'supra']
segona_llista = ['campió', 'campiona']
connector = '-'
resultat = concatena_llistes(primera_llista, segona_llista, connector)
print(resultat)