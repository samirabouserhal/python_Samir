#Programme de questionnement
print("Chosis la couleur rouge ou bleu")
choix=input().lower()


if choix=="bleu":
    print("")
    print("Vous avez choisi bleu")
    print("Aimez vous la couleur bleu, oui ou non")
    choix2=input().lower()
    if choix2=="oui":
        print("Donc vous aimez la couleur bleu, moi aussi!!")
    if choix2=="non":
        print("Donc vous n'aimez pas la couleur bleu")


if choix=="rouge":
    print("")
    print("Vous avez chosi rouge")
    print("Aimez vous la couleur rouge, oui ou non")
    choix2=input().lower()
    if choix2=="oui":
        print("Donc, vous aimez la couleur rouge, moi aussi!!!")
    if choix2=="non":
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
print("Vous avez", age, "année?! WOW!")

