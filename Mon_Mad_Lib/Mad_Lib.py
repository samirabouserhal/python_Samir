phrases = []
consignes = []

# changer seulement les lignes dans mon_mad_lib ci-dessous
# --> supprimer les phrases.append et consignes.append
# --> ajouter vos propres phrases et consignes
#
# NE CHANGER RIEN D'AUTRE DANS LE PROGRAMME
#
# Si tout le monde fais ça, je vais pouvoir intégrer le
# travail dans un "livre" de mad libs que vous pourrez
# jouer avec votre famille pendant le temps des fêtes
#

def mon_mad_lib():
    """Préparer les phrases à trou""" 

    # le trou dans la phrase est indiqué par les {}
    phrases.append("Vous quitez pour le/la/l' {} à 8:00 ce matin")
    consignes.append("lieu")

    phrases.append("Vous arivez à {}")
    consignes.append("un temps")

    phrases.append("Vous êtes là pour {}")
    consignes.append("verbe")

    phrases.append("Vous voyez le/la/l' {}")
    consignes.append("personne")

    phrases.append("Il/Elle est {}")
    consignes.append("adjectif")

    phrases.append("Vous quittez pour aller chez {}")
    consignes.append("restaurant")

    phrases.append("Le retaurant est {}")
    consignes.append("adjectif")

    phrases.append("Votre {} vous appele")
    consignes.append("personne")

    phrases.append("Il/Elle vous dit de faire le/la {}")
    consignes.append("tâche à faire")

    phrases.append("Vous allez à {}")
    consignes.append("magasin")

    phrases.append("Il est {}")
    consignes.append("temps")

    phrases.append("Vous retournez chez {}")
    consignes.append("lieu")

    phrases.append("Vous {} de l'eau")
    consignes.append("verbe du premier groupe")

    phrases.append("Il est temps de {}")
    consignes.append("verbe")

    phrases.append("Vous êtes un/une {}")
    consignes.append("mot")





mon_mad_lib()

# Obtenir les réponses de l'utilisateur
mots = []
# on demande un mot pour chaque consigne, utilisant la boucle 'for each'
for c in consignes:
    # ici le print utilise la méthode .format() qui remplace chaque {}
    # dans le texte avec la valeur dans le .format()
    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())


# Afficher le résultat
print("Quand tu est prêt(e) pour le résultat, tape Enter")
input() # attend

for i in range(len(phrases)):
    # les trous {} dans les phrases sont remplacés par les mots.
    print(phrases[i].format(mots[i]))

print("\nMerci d'avoir joué!")