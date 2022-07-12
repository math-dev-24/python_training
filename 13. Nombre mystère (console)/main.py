import random

NBR_MYSTERE = random.randint(0,100)
NBR_ESSAI = 6
NBR_TEST = 0

print("** Le jeu du nombre mystère entre 0 et 100 **")
while NBR_ESSAI > 0:
    nbr = input("Devine le nombre : >")
    try:
        nbr = int(nbr)
        NBR_TEST += 1
    except:
        print("Veuillez rentrez un nombre Valide")
    else:
        if nbr == NBR_MYSTERE:
            print(f"Bravo. tu as trouvé en {NBR_TEST}")
        if nbr >= NBR_MYSTERE:
            NBR_ESSAI -= 1
            print(f"Le nombre mystère est plus petit. \n Il reste {NBR_ESSAI} essais")
        if nbr <= NBR_MYSTERE:
            NBR_ESSAI -= 1
            print(f"Le nombre mystère est plus grand. \n Il reste {NBR_ESSAI} essais")

if NBR_ESSAI == 0:
    print(f"Tu as perdu. Le nombre mystère été {NBR_MYSTERE}")