repertoire = {}
repertoire["roland"] = "060609606"
repertoire["roger"] = "56496874987"

def lister_repertoire(repertoire):
    print(repertoire)

def ajouter_a_repertoire(repertoire):
    nom = input("entrez un nom : ")
    numero = input("entrez un numéro : ")
    repertoire[nom] = numero

def supprimer_contact(repertoire):
    nom_contact = input("saisir nom du contact à suppr : ")
    del repertoire[nom_contact]


# UI
while True :
    saisie_utilisateur = input("a = ajouter, l = lister, s = suppr : ")
    if saisie_utilisateur == "l":
        lister_repertoire(repertoire)
    if saisie_utilisateur == "a":
        ajouter_a_repertoire(repertoire)
    if saisie_utilisateur == "s":
        supprimer_contact(repertoire)
