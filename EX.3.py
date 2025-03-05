"""
Crear una funció que donada una llista de paraules i una lletra, retorni una llista amb les paraules que comencen per la lletra donada. Utilitzar filter. 
Ex: [“maria”, “manta”, “peu”, “mà”] i li deim que ens retorni totes les que comencen per ‘p’, en retorni [‘peu’].
"""
def paraules_que_comencen_per(paraules, lletra):
    if len(lletra) != 1:
        raise ValueError("La lletra ha de ser un sol caràcter")

    paraules_resultat = list(filter(lambda paraula: paraula.startswith(lletra), paraules))

    return paraules_resultat

llista_paraules = ["maria", "manta", "peu", "mà"]
lletra = "p"
resultat = paraules_que_comencen_per(llista_paraules, lletra)
print(resultat)