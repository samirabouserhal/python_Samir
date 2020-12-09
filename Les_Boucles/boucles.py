boucle=True
print("Voici le menu informatique du jour.")
print("Je m'appelle Rob, et vous êtes?")
nom=input()
print("Bonjour", nom)
print("Les options vous seront présentés entre guillemets")
while boucle:
  print("Vos options sont:")
  print("De 'compter' de 1 à 10")
  print("Et de 'répéter' vos choix")
  print("De 'quitter' le menu")
  choix=input().lower()
  
  if choix=="compter":
    boucle=False
    repeat=True
    for i in range(1,11):
      print(i)
    print("Merci beaucoup", nom,"à la prochaine.")
  
  elif choix=="répéter":
    boucle=True
    print("Bien sure", nom)
  
  elif choix=="quitter":
    boucle=False
    print("Peut-être on se revera un jour",nom,". À la prochaine.")