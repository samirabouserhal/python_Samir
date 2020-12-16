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
    
    phrases.append("Vous allez chez le/la/l' {}")
    consignes.append("lieu")

    phrases.append("Vous entrez pour prendre un/une {}")
    consignes.append("objet")

    phrases.append("Vous quittez pour le donner au {}")
    consignes.append("personne")

    phrases.append("Il vous dit {}")
    consignes.append("mot")

    phrases.append("Vous êtes maintenant {}")
    consignes.append("adjectif")

    phrases.append("Vous quittez pour aller chez {} ")
    consignes.append("lieu")

    phrases.append("Vous êtes là pour {}")
    consignes.append("verbe")

    





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