"""
Crear una funció que donada una llista de valors numèrics, retorni el número d’elements on coincideix el valor i l’índex on és. 
Utilitzar enumerate. Ex: [0, 2, 3, 3, 4], retorni 3.
"""
def compta_valors_iguals_a_index(llista):
    return sum(1 for index, valor in enumerate(llista) if index == valor)

llista = [0, 2, 3, 3, 4]
resultat = compta_valors_iguals_a_index(llista)
print(resultat)