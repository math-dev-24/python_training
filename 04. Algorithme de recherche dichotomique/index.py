import random

max_ = random.randint(100,350)
min_ = random.randint(-100,25)
nombre_recherche = -200
nombre_test = -20000000
is_valid = True

while nombre_recherche <= min_ or nombre_recherche >= max_:
    nombre = input(f"Quel est votre nombre ? (entre {min_} et {max_}) > ")
    if nombre.isnumeric():
        nombre_recherche = int(nombre)
    else:
        print('Nombre demandé')

while is_valid:
    nombre_test = round((max_ + min_) / 2)

    if nombre_recherche == nombre_test:
        print(f"Nombre testé : {nombre_test}, nombre à trouver {nombre_recherche}")
        is_valid = False
    else:
        if nombre_test < nombre_recherche:
            print(f"Nombre testé : {nombre_test}. Trop petit")
            min_ = nombre_recherche
        else:
            print(f"Nombre testé : {nombre_test}. Trop Grand")
            max_ = nombre_recherche
