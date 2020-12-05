# Ceci est le lieu de travail de Samir Abou Serhal pour son travail sommatif de programme interactif
# Ce document fut créer le 3 décembre 2020 et modifier le 6 décembre 2020
# Pour me contacter, envoyer un couriel à abosam@ecolecatholique.ca

print("S'il vous plaît insérer votre nom:")
nom= input()
print("")
print("Bonjour", nom,", j'ai besoin de votre aide. La princesse du royaume Guimauve, ma chère fille, fut kidnappé et vous êtes la seul personne qui puisse la sauvé.") 
print("Lors de cette aventure, je vous présentera des choix qui se retrouveront entre guillemets. S'il vous plaît soigner votre ortographe")
print("Cette mission sera difficile, mais sa serait un petit défi pour un chevalier comme vous.")
print("")
print("Voici votre premier choix")
print("Accepter vous la mission de sauvé la princess du royaume des guimauves, 'oui' ou 'non'.")


# Code qui décide si l'aventure commence ou non

choix1=input().lower()
if choix1=="oui":
    estOui= True
    print("")
    print("Merci beaucoup", nom, "je vous récompensera pour votre bravoure plus-tard.") 
    print("Le Mage Gandalf vous accompagnera sur votre aventure pour vous donner des conseils.")
elif choix1=="non":
    print("")
    print("Je ne comprends pas, voulez vous laiser la princess mourir toute seule? 'oui' je veux la laisser mourir ou 'non' je vais la sauver")
    choix2=input().lower()
    if choix2=="oui":
        estOui=False
        print("")
        print("Vous êtes bani du royaume des guimauves. Si je vous vois encore, vous serez éxécuter.")
        print("")
        print("GAME OVER")
    elif choix2=="non":
        estOui=True
        print("")
        print("Donc vous allez sauvé la princess?", nom,)
    else:
      print("Je m'excuse, je n'ai pas compris votre choix. Je présume que vous avez dit oui et que vous allez laissez la princess mourir.")
      print(" Dans ce cas, vous êtes bani du royaume des guimauves et si je vous vois encore, vous serez éxécuter.")
      print("")
      print("GAME OVER")
      estOui=False
else: 
    print("Je m'excuse, je n'ai pas compris ce que vous avez écris." "Je présume que votre réponse est non.")
    estOui=False
    print("")
    print("GAME OVER")
if estOui==True:
    print("Merci d'avoir choisi de sauver la princess. Votre aventure commence maintenant.")
    print("")
    print("Pèse enter pour continuer")
    Pour_continuer=input()



# Premier problème

if estOui==True:
    print("")
    print("La princess fut transporté vers le royaune de Kit Kat au sud du royaume de Guimauve.")
    print("Le Mage Gandalf est très familier avec se royaume et il te guidera vers le chateau où ma chère fille est détenu.")
    print("")
    print("Bonjour", nom, ", je suis le Mage Gandalf. J\'aimerais quité avant le couché du soleil, donc alons-y!")
    print("")
    print("Le Soleil se couche, on devrait se reposer la nuit")
    print("Le Mage et", nom,"s'endorme autour du feu de camp que le mage a allumer")
    print("")
    print("Pèse enter pour continuer")
    Pour_continuer=input()

    print(nom.upper(), "RÉVEILLE-TOI, ON SE FAIT ATTACKER PAR DES GOBLINS!!!")
    print(nom.upper(),"LES GOBLINS ONT PEUR DU FEU. PREND UNE BRANCHE DU FEU DE CAMP POUR NOUS DÉFENDRE")
    print("")
    print("Qu'est-ce que vous aller faire, allez vous prendre le 'feu' ou aller vous sortir votre 'épée'")
    choix3=input().lower()

    if choix3=="feu":
        estOui=True
        print("Vous avez sauvé la vie du Mage et la votre, félicitation")
    elif choix3=="épée":
        estOui=False
        print("Les goblins ne peuvent pas être tué par ton épée. Ils ont gagnés la bataille et vous avez été tués.")
        print("")
        print("GAME OVER")
    else:
      print("Je m'excuse, je n'ai pas compris votre réponse. Je présume que vous avez ignorez les conseils du Mage et que vous avez étés vaincus par les goblins")
      print("")
      print("GAME OVER")
      estOui=False

if estOui:
  print("")
  print("Après avoir gagné contre les goblins, vous avez continuer votre aventure vers le royaume de Kit Kat.")
  print("")  
  print("Deux jours on passé et vous avez finalement atteint le chateau du royaume sans aucun nouveau problème.")
  print("Vous avez maintenant deux options. Vous pouvez soit infiltrer le chateau 'silencieusement', ou vous pouvez entré 'bruyant'" )
  choix4=input().lower()
  if choix4=="silencieusement":
    print("Donc vous voulez entré silencieusement?")
    print("Il faut maintenant choisir où infiltrer")
    print("Vous pouvez soit vous 'déguisé' comme des servants en utilisant la magie du Mage, ou vous pouvez entré en utilisant le système de 'ventilation'")
    choix5=input().lower()
    if choix5="déguisé":
      print("Vous avez infiltré le chateau avec succès!!")
      print("Tu peux commencé la recherche pour la princess")
      estOui=True
    elif choix5="ventilation":
      print("Vous avez essayer d'utiliser le système de ventilation, mais votre épée fesait trop de bruit contre les conduits d'air et vous avez été découvert et emprisonné")
      estOui=False
  elif: choix4="bruyant":
    print("En choisisant l'entré 'bruyant', vous allez entré par force par la porte principal")
    print("Êtes-vous certain que vous voulez choisir cette méthode pour sauver la princess")

    