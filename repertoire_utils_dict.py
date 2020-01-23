repertoire = [{"nom": "marc", "numero": "06060606", "adresse": "par là"},
              {"nom": "ok", "numero": "0707070707", "adresse": "par ici"}]


def get_rep():
    return repertoire


def append_rep(repertoire, personne):
    repertoire.append(personne)


def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)


def lister_les_contacts(repertoire):
    return repertoire
