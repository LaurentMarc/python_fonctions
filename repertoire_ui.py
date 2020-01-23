import repertoire_action as action
from terminaltables import AsciiTable

def lister_repertoire(repertoire):
    affichage_tableau(action.lister_contacts(repertoire))

def affichage_tableau(contacts_a_afficher):
    tableau = [["NOM", "TEL", "ADRESSE"]]
    for contact in contacts_a_afficher:
        tableau.append([contact["nom"], contact["numero"], contact["adresse"]])
    tableau_table = AsciiTable(tableau)
    print(tableau_table.table)

def ajouter_a_repertoire(repertoire):
    nom = input("entrez un nom : ")
    numero = input("entrez un numéro : ")
    adresse = input("entrez une adresse : ")

    action.ajouter_personne(repertoire, nom, numero, adresse)
    affichage_tableau(repertoire)


def supprimer_contact(repertoire):
    nom = input("saisir nom du contact à suppr : ")
    action.supprimer_personne(repertoire, nom)
    affichage_tableau(repertoire)


def recherche_contact(repertoire):
    while True:
        saisie_recherche = input("Rechercher par : n = nom, t = telephone, a = adresse, q = quitter : ").lower()
        if saisie_recherche == "n":
            saisie_recherche = input("entrez nom à rechercher : ")
            affichage_tableau(action.chercher_personnes(repertoire, saisie_recherche, "nom"))
        if saisie_recherche == "t":
            saisie_recherche = input("entrez téléphone à rechercher : ")
            affichage_tableau(action.chercher_personnes(repertoire, saisie_recherche, "numero"))
        if saisie_recherche == "a":
            saisie_recherche = input("entrez adresse à rechercher : ")
            affichage_tableau(action.chercher_personnes(repertoire, saisie_recherche, "adresse"))
        if saisie_recherche == "q":
            break

# UI
while True:
    repertoire = action.get_rep_action()
    saisie_utilisateur = input("a = ajouter, l = lister, s = suppr, r = rechercher, q = quitter : ").lower()
    if saisie_utilisateur == "l":
        lister_repertoire(repertoire)
    if saisie_utilisateur == "a":
        ajouter_a_repertoire(repertoire)
    if saisie_utilisateur == "s":
        supprimer_contact(repertoire)
    if saisie_utilisateur == "r":
        recherche_contact(repertoire)
    if saisie_utilisateur == "q":
        break
