# Lieu de travail de Samir Abou Serhal pour le travail de liste
# La date est le 17 décembre 2020
# Pour me contacter, envoyer moi un couriel à abosam30@ecolecatholique.ca




print("")
print("Bonjour, je suis un menu interactif.")
print("Voici les options que je vous présente:")
print("")
print("Pèse 0 pour dire bonjour.")
print("Pèse 1 pour savoir mon nom.")
print("Pèse 2 pour dire comment s\'a vas.")
print("Pèse 3 pour épelé aujourd'hui.")
print("Pèse 4 pour dire merci.")
print("Pèse 5 pour dire de rien.")
print("Pèse 6 pour dire tous les mots.")
print("Pèse 7 pour répéter tes options.")
print("Pèse 8 pour quitter le menu interactif.")

boucle=True

mots=["Bonjour", "Mon nom est Rob", "Comment s'a va", "Aujourd'hui", "Merci", "De rien", "Répète", "Quitter"]

while boucle:

    choix=input().lower()

    if choix=="0":
        print(mots[0])
        boucle=True
   
    elif choix=="1":
        print(mots[1])
        boucle=True
    
    elif choix=="2":
        print(mots[2])
        boucle=True
    
    elif choix=="3":
      for lettre in (mots[3]):
        print(lettre)
        boucle=True

    elif choix=="4":
        print(mots[4])
        boucle=True
   
    elif choix=="5":
        print(mots[6])
        boucle=True

    elif choix=="6":
        for i in range(len(mots)):
          print(mots[i])

    elif choix=="7":
        boucle=True
        print("Pèse 0 pour dire bonjour.")
        print("Pèse 1 pour savoir mon nom.")
        print("Pèse 2 pour dire comment s\'a vas.")
        print("Pèse 3 pour épelé aujourd'hui.")
        print("Pèse 4 pour dire merci.")
        print("Pèse 5 pour dire de rien.")
        print("Pèse 6 pour dire tous les mots.")
        print("Pèse 7 pour répéter tes options.")
        print("Pèse 8 pour quitter le menu interactif.")

    elif choix=="8":
        print(mots[7])
        boucle=False
        print("Merci pour votre temps, à la prochaine.")
   
    else:
        print("Votre entré n'est pas valide, s'il vous plaît essayer encore")
    

