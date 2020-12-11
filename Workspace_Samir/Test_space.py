#Programme de comparaison et de elif
#Par : Samir Abou Serhal    abosam30@ecolecatholique.ca
# 2020-12-01

"""
print("Chosis la couleur rouge ou bleu")
choix=input().lower()


if choix=="bleu":
    print("")
    print("Vous avez choisi bleu")
    print("Aimez vous la couleur bleu, oui ou non")
    choix2=input().lower()
    if choix2=="oui":
        print("Donc vous aimez la couleur bleu, moi aussi!!")
    elif choix2=="non":
        print("Donc vous n'aimez pas la couleur bleu")


elif choix=="rouge":
    print("")
    print("Vous avez chosi rouge")
    print("Aimez vous la couleur rouge, oui ou non")
    choix2=input().lower()
    if choix2=="oui":
        print("Donc, vous aimez la couleur rouge, moi aussi!!!")
    elif choix2=="non":
        print("Donc vous n'aimez pas la couleur rouge")

if choix2=="non":
    print("")
    print("Quelle est vore couleur préféré?")
    choix3=input().lower()
    print(choix3,"est une merveilleuse couleur, je l'aime aussi!!!")

print("")
print("On aime la même couleur, c'est quoi votre nom?")
nom= input()
print("Bonjour", nom,"je suis content de faire votre connaissance, je m'appelle  Arc.")
print("Vous avez quelle age?")
age=input()
print("Vous avez", age, "ans?! WOW!!!")
"""

# Nouveau projet
"""
print("oui ou non")
choix=input().lower()
if choix=="oui":
    print("Vous avez choisi oui")
elif choix=="non":
    print("Vous avez choisi non")
else:
    print("Je m'excuse, je n'ai pas compris", choix, "pouvez vous recommencer s'il vous plaît.")
    """
"""
estOui=True
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
            #choix5=input().lower()
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
                repeat2=False
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
                    #Je ne sait pas pourquoi ce choix uniquement nécésittent deux input lors d'une erreur
                    repeat2=True
                    #choix7=input().lower()
        
            else:
                print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
                repeat2=True
                choix6=input().lower()
    else:
        print("Je m'excuse, je n'ai pas compris ce que vous avez écris. Je vous donne une autre chance de répondre à la question.")
        repeat2=True
        choix4=input().lower()
"""

"""
# EXEMPLE DE BOUCLE

print("oui ou non")
repeat=True
choix=input().lower()
while repeat:
    if choix=="oui":
        print("Vous avez chosis oui")
        repeat=False
        repeat2=True
        print("rouge ou bleu")
        choix2=input().lower()
        while repeat2:
            if choix2=="rouge":
                print("vous avez choisis rouge")
                repeat2=False
            elif choix2=="bleu":
                print("vous avez choisis bleu")
                repeat2=False
            else:
                print("Didn't understand")
                repeat2=True
                choix2=input().lower()
    elif choix=="non":
        print("Vous avez choisis non")
        repeat=False
        repeat3=True
        print("vert ou jaune")
        choix3=input().lower()
        while repeat3:
            if choix3=="vert":
                print("vous avez choisis vert")
                repeat3=False
            elif choix3=="jaune":
                print("vous avez choisis jaune")
                repeat3=False
            else:
                print("Didn't understand")
                repeat3=True
                choix3=input().lower()
    else:
        print("Didn't understand")
        repeat=True
        choix=input().lower()




print("")
print("")
print("up or down")
boucle=True
user=input().lower()
while boucle:
    if user=="up":
        print("going up")
        boucle=False
        boucle1=True 
        print("pizza ou chien chaud")
        user1=input().lower()
        while boucle1:
            if user1=="pizza":
                print("Vous avez choisis la pizza")
                boucle1=False
            
            elif user1=="chien chaud":
                print("Vous avez choisis le chien chaud")
                boucle1=False

            else:
                print("Je n'ai pas compris")
                boucle1=True
                user1=input().lower()

    
    elif user=="down":
        boucle=False
        print("You're going down")
        boucle3=True
        user2=input().lower()
        print("tôt ou tard")
        while boucle3:
            if user2=="tôt":
                print("Félicitation, vous êtes tôt")
                boucle3=False

            elif user2=="tard":
                print("Vous êtes en retard")
                boucle3=False

            else:
                print("Je n'ai pas compris")
                boucle3=True
                user2=input().lower()
    
    else:
        print("Je n'ai pas compris")
        boucle=True
        user=input().lower()

        """

print("Insère un nombre pour qu'il puisse être classés en trois catégorie:")
print("Positif, Zero, Negatif")
x=input().lower()

boucle=True
while boucle:
    x=float(x)
    if x==0:
        print("Zero")

    elif x>=0:
        print("Positif")

    elif x<=0:
        print("Negatif")
    
    print("")
    print("Pour insérer un autre nombre, pèse sur e")
    print("Pour quitter, pezer sur n'importe quelle autre clé")
    y=input().lower()

    if y=="e":
        boucle=True
        print("Vous avez recommencer")
        print("Insère un autre nombre")
        x=input().lower()

    elif y !="e":
        boucle=False
        print("Vous avez quitter le programme")
        print("Merci pour votre temps")

