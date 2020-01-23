import json


def get_rep():
    fichier = open("data.txt", "r")
    repertoire = json.loads(fichier.read())
    fichier.close()
    return repertoire


def append_rep(repertoire, personne):
    repertoire.append(personne)
    with open("data.txt", "w") as fichier:
        fichier.write(json.dumps(repertoire))


def del_rep(repertoire, personne):
    for contact in repertoire:
        if contact["nom"] == personne:
            repertoire.remove(contact)
    with open("data.txt", "w") as fichier:
        fichier.write(json.dumps(repertoire))


def lister_les_contacts(repertoire):
    contacts = []
    for contact in repertoire:
        contacts.append(contact)
    return contacts
