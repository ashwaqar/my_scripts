"""We are going to save a txt file with all the files in your directory.
We will use the function walk()

"""

import os

# see all the methos of os
# print(*dir(os), sep=", ")
listafile = []
percorso = []
with open("lista_file.txt", "w") as testo:
    for root, dirs, files in os.walk("."):
        for file in files:
            listafile.append(file)
            percorso.append(root + "\\" + file)
            testo.write(file + "\n")
listafile.sort()
print("N. of files", len(listafile))
with open("lista_file_ordinata.txt", "w") as testo_ordinato:
    for file in listafile:
        testo_ordinato.write(file + "\n")

with open("percorso.txt", "w") as file_percorso:
    for file in percorso:
        file_percorso.write(file + "\n")

os.system("lista_file.txt")
os.system("lista_file_ordinata.txt")
os.system("percorso.txt")
