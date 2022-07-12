import sys

QUESTION ="""_______________________________________________________________________
Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la la liste 
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
>> Votre choix :  """
MENU_CHOICES = ["1","2","3","4","5"]
data_table = []

while True:
    response = ""
    while response not in MENU_CHOICES:
        response = input(QUESTION)
        if response not in MENU_CHOICES:
           print("Veuillez choisir une option valide ...")
    if response == "5":
        sys.exit()
    if response == "1":
        data_add = input("Entrez le nom de l'élément à ajouter : ")
        data_table.append(data_add)
    if response == "2":
        data_del = input("Entrez l'élément à supprimer : ")
        try:
            data_table.remove(data_del)
            print(f"l'élement {data_del} à été supprimé")
        except:
            print("l'élement n'existe pas.")
    if response == "3":
        if not data_table:
           print("liste vide")
        print("Liste : ")
        for i, item in enumerate(data_table):
            print(i+1, item)
    if response == "4":
        data_table.clear()
        print("Liste vidée")