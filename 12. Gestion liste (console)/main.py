import sys
import os
import json

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

if os.path.exists(LISTE_PATH):
    with open(LISTE_PATH, "r") as f:
        LISTE = json.load(f)
else:
    LISTE = []

QUESTION ="""_______________________________________________________________________
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la la liste 
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
>> Votre choix :  """
MENU_CHOICES = ["1","2","3","4","5"]

while True:
    response = ""
    while response not in MENU_CHOICES:
        response = input(QUESTION)
        if response not in MENU_CHOICES:
           print("Veuillez choisir une option valide ...")
    if response == "5":
        with open(LISTE_PATH,"w") as f:
            json.dump(LISTE, f, indent=4)
        print("A bientôt !")
        sys.exit()
    if response == "1":
        data_add = input("Entrez le nom de l'élément à ajouter : ")
        LISTE.append(data_add)
    if response == "2":
        data_del = input("Entrez l'élément à supprimer : ")
        try:
            LISTE.remove(data_del)
            print(f"l'élement {data_del} à été supprimé")
        except:
            print("l'élement n'existe pas.")
    if response == "3":
        if not LISTE:
           print("liste vide")
        print("Liste : ")
        for i, item in enumerate(LISTE):
            print(i+1, item)
    if response == "4":
        LISTE.clear()
        print("Liste vidée")