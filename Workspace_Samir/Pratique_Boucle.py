# Ceci est le lieu de pratique de Samir Abou Serhal
# Contacter moi à abosam30@ecolecatholique.ca
# Le 8 décembre 2020


#Introduction

print("S'il vous plaît insérer votre nom:")
nom= input()
print("")
print("Bonjour", nom,", j'ai besoin de votre aide. La princesse du royaume Guimauve, ma chère fille, fut kidnappé et vous êtes la seul personne qui peut la sauvé.") 
print("Lors de cette aventure, je vous présentera des choix qui se retrouveront entre guillemets. S'il vous plaît soigner votre ortographe")
print("Cette mission sera difficile, mais sa serait un petit défi pour un chevalier comme vous.")
print("")
print("Voici votre premier choix")
print("Accepter vous la mission de sauvé la princess du royaume des guimauves, 'oui' ou 'non'.")


# Code qui décide si l'aventure commence ou non

choix1=input().lower()
repeat=True
while repeat:
    if choix1=="oui":
        estOui= True
        print("")
        print("Merci beaucoup", nom, "je vous récompensera pour votre bravoure plus-tard.") 
        print("Le Mage Gandalf vous accompagnera sur votre aventure pour vous donner des conseils.")
        repeat=False
    elif choix1=="non":
        print("")
        print("Je ne comprends pas, voulez vous laiser la princess mourir toute seule? 'oui' je veux la laisser mourir ou 'non' je vais la sauver")
        choix2=input().lower()
        while repeat:
            if choix2=="oui":
                estOui=False
                print("")
                print("Vous êtes bani du royaume des guimauves. Si je vous vois encore, vous serez éxécuter.")
                print("")
                print("GAME OVER")
                repeat=False
            elif choix2=="non":
                estOui=True
                print("")
                print("Donc vous allez sauvé la princess?", nom,)
                repeat=False
            else:
                print("Je m'excuse, je n'ai pas compris. Je vous donne une autre chance de répondre à la question.")
                choix2=input().lower()
                repeat=True

    else:
        print("Je m'excuse, je n'ai pas compris. Je vous donne une autre chance de répondre à la question.")
        choix1=input().lower()
        repeat=True
       

    
if estOui==True:
    print("Merci d'avoir choisi de sauver la princess. Votre aventure commence maintenant.")
    print("")
    print("Pèse enter pour continuer")
    Pour_continuer=input()



# Première décision

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
    repeat1=True
    while repeat1:
        if choix3=="feu":
            estOui=True
            print("Vous avez sauvé la vie du Mage et la votre, félicitation")
            repeat1=False
        elif choix3=="épée":
            estOui=False
            print("Les goblins ne peuvent pas être tué par ton épée. Ils ont gagnés la bataille et vous avez été tués.")
            print("")
            print("GAME OVER")
            repeat1=False
        else:
            print("Je m'excuse, je n'ai pas compris. Je vous donne une autre chance de répondre à la question.")      
            repeat1=True
            choix3=input().lower()
        
                

# Deuxième décision et troisième décision

if estOui:
  print("")
  print("Après avoir gagné contre les goblins, vous avez continuer votre aventure vers le royaume de Kit Kat.")
  print("")  
  print("Deux jours on passé et vous avez finalement atteint le chateau du royaume sans aucun nouveau problème.")
  print("Vous avez maintenant deux options. Vous pouvez soit infiltrer le chateau 'silencieusement', ou vous pouvez entré 'bruyant'" )
  choix4=input().lower()
  repeat2=True
  while repeat2:
    if choix4=="silencieusement":
        print("Donc vous voulez entré silencieusement?")
        print("Il faut maintenant choisir comment infiltrer")
        print("Vous pouvez soit vous 'déguisé' comme des servants en utilisant la magie du Mage, ou vous pouvez entré en utilisant le système de 'ventilation'")
        choix5=input().lower()
        if choix5=="déguisé":
            print("Vous avez infiltré le chateau avec succès!!")
            print("Tu peux commencé la recherche pour la princess")
            estOui=True
            repeat2=False
        elif choix5=="ventilation":
            print("Vous avez essayer d'utiliser le système de ventilation, mais votre épée fesait trop de bruit contre les conduits d'air et vous avez été découvert et emprisonné")
            print("")
            print("GAME OVER")
            estOui=False
            repeat2=False
        else:
            print("Je m'excuse, je n'ai pas compris votre choix. Je vous donne une autre chance de répondre à la question.")
            repeat2=True
            choix5=input().lower()
    elif choix4=="bruyant":
        print("En choisisant l'entré 'bruyant', vous allez entré par force par la porte principal")
        print("Êtes-vous certain que vous voulez choisir cette méthode pour sauver la princess?")
        print("'oui' ou 'non'")
        choix6=input().lower()
        repeat2=True
        while repeat2:
            if choix6=="oui":
                print("Vous avez entré par la porte principale et vous avez été découvert par les guardiens du chateau. Ils vous ont emprisonnés")
                print("")
                print("GAME OVER")
                repeat2=False
                estOui=False
            elif choix6=="non":
                print("En choisissant cette option vous optez pour l'option 'silencieusement'")  
                print("Voici tes options:")
                print("Tu peux soit te 'déguisé' comme un servant à l'aide de la magie du mage, ou infiltrer le chateau à l'aide du système de 'ventilation' ")
                choix7=input().lower()
                if choix7=="déguisé":
                    print("Vous avez infiltré le chateau avec succès!!")
                    print("Tu peux commencé la recherche pour la princess")
                    estOui=True
                    repeat2=False
                elif choix7=="ventilation":
                    print("Vous avez essayer d'utiliser le système de ventilation, mais votre épée fesait trop de bruit contre les conduits d'air et vous avez été découvert et emprisonné")
                    print("")
                    print("GAME OVER")
                    estOui=False
                    repeat2=False
                else:
                    print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
                    print("Pèse enter pour entre une nouvelle réponse.") #Je ne sait pas pourquoi ce choix uniquement nécésittent deux input lors d'une erreur
                    repeat2=True
                    choix7=input().lower()
        
            else:
                print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
                repeat2=True
                choix6=input().lower()
    else:
        print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
        repeat2=True
        choix4=input().lower()
        


# Dernière décision

if estOui:
  print(nom,", tu es maintenant dans le chateau")
  print("Le mage utilise sa magie et trouve la princess")
  print("Vous allez la sauvé, mais quand vous entré, ce que vous voyez vous surprise")
  print("")
  print("La princess du royaume de Guimauve et le prince du royaume des Kit Kat sont en train de diner ensemble")
  print("Tous les deux sont contents")
  print("La princess vous dit qu'elle est content avec le prince et qu'elle va le marrié")
  print("")
  print("Vous retourné au royaume de Guimauve et vous informez le roi")
  print("Il vous demande si il devrait laisser sa fille se 'marier' ou de la forcer à retourner à la 'maison'")
  repeat3=True
  while repeat3:
    choix8=input().lower()
    if choix8=="marier":
        print("Vous avez raison", nom, ", si elle est content je devrais lui laisser le marrier")
        estOui=True
        repeat3=False
    elif choix8=="maison":  
        print("Ne voulez vous pas que ma fille soit contente")
        print("Vous êtes quand même trop jeune pour comprendre alors")
        print("")
        print("GAME OVER")
        estOui=False  
        repeat3=False
    else:
        print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
        estOui=False
        repeat3=True

# conclusion 


if estOui:
  print("Le mariage resultat dans une alliance entre les deux royaumes et une ère de paix la suivi")
  print("La princess ne s'était pas fait kidnappé, mais vous avez quand même sauvé le royaume")
  print("Merci", nom)
  print("")
  print("game over")