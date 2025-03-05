"""
Crear un directori dins /home/cicles/AO que es digui Prova, canviar-nos a aquest directori, a dins, crear el fitxer Ex12.txt i posar a dins el nom de tots els companys de classe. 
Tancar el fitxer. Obrir-lo per afegir el nom dels professors. Tancar-lo. Finalment, l’obrirem i posarem tot el seu contingut dins una llista de noms.
"""
import os

directori = '/home/cicles/AO/Prova'
os.makedirs(directori, exist_ok=True)

os.chdir(directori)

noms_companys = ["Oscar Borras Riutort","Marc Caldas Garrido","Jaume Cardona Andreu","Iker Javier Delicado Rus","Juan Pablo Fuentes de Vera","Eneko Gomez Diaz","Pau Gomila Barber","Pere Gomila Cuevas","Ivan Hordieiev","Aris Krysak Tomas","Brais Jordan Manent Miranda","Antonio Martinez Martinez","Jordi Meliá Carreras","Alejandra Moya Zamora","Ivan Muñoz León","Lucas Perelló Bagur","Adrian Perez Calderon","Yago Pons Garcia Boente","David Sánchez Cabanillas","Gustavo Tecchio Neiva","Bruno Aimé Vaca Mendoza","Alejandro Vallecillo Vaca","Saad Zaidi Zaid"]
with open('Ex12.txt', 'w') as fitxer:
    for nom in noms_companys:
        fitxer.write(nom + '\n')

noms_professor = ["Joan Carreras Vinent"]
with open('Ex12.txt', 'a') as fitxer:
    for nom in noms_professor:
        fitxer.write(nom + '\n')

with open('Ex12.txt', 'r') as fitxer:
    llista_noms = fitxer.read().splitlines()

print(llista_noms)  