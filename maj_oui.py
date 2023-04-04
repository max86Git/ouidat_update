import requests

lignes = []
resultats = []
i = 0
fichier = ""

url = "http://standards-oui.ieee.org/oui/oui.txt"
response = requests.get(url)
data = response.text
lignes = data.splitlines()

for ligne in lignes:
    if ligne.count("(base 16)") > 0:
        resultats.append(ligne[:6] + "\t" + ligne[22:])

list.sort(resultats)

for resultat in resultats:
    fichier += resultat + "\n"

fichier += "### Fin : " + str(len(resultats)) + " entrées\n"

with open("oui.dat", "a", encoding="utf-8") as f:
    f.write(fichier)


