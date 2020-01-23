# import repertoire_utils_dict as repertoire_utils


import repertoire_utils_text as repertoire_utils


def chercher_personnes(repertoire, saisie_recherche, key):
    resultat = []
    for contact in repertoire_utils.lister_les_contacts(repertoire):
        if contact[key] == saisie_recherche:
            resultat.append(contact)
    return resultat


def ajouter_personne(repertoire, nom, numero, adresse):
    personne = {"nom": nom, "numero": numero, "adresse": adresse}
    repertoire_utils.append_rep(repertoire, personne)


def supprimer_personne(repertoire, personne):
    repertoire_utils.del_rep(repertoire, personne)


def get_rep_action():
    return repertoire_utils.get_rep()


def lister_contacts(repertoire):
    return repertoire_utils.lister_les_contacts(repertoire)
