from random import *
min, max = 0, 10
price_to_guess = randint(min,max)
input_user = -1
while price_to_guess != input_user:
    input_user = int(input(f"Quel est le juste prix ? (entre {min}-{max} ) > "))
    if input_user != price_to_guess:
        print('Plus petit') if input_user > price_to_guess else print('Plus Grand')
print("Bravo, Vous avez trouvé")