import random


class Player:
    def __init__(self, nom):
        self.name = nom
        self.life = 50
        if self.name == "bot":
            self.potion_of_life = 0
        else:
            self.potion_of_life = 3

    def use_potion_of_life(self):
        self.potion_of_life -= 1
        life_restore = random.randint(15, 50)
        self.life += life_restore
        return life_restore

    def atk_player(self):
        if self.name == "bot":
            return random.randint(5, 15)
        else:
            return random.randint(5, 10)


name = ""
while name == "":
    name = input("Quel est votre pseudo ?  ")
JOUEUR = Player(name)
BOT = Player("bot")
LIST_CHOICES = ["1","2"]

while BOT.life > 0 and JOUEUR.life > 0:
    print(f"{JOUEUR.name} : {JOUEUR.life} vies et {JOUEUR.potion_of_life} potions")
    print(f"{BOT.name} à {BOT.life} vies")
    action = ""
    while action not in LIST_CHOICES:
        action = input(f"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? > ")
        print("")
    if action == "1":
        atk = JOUEUR.atk_player()
        BOT.life -= atk
        if BOT.life < 1:
            print(f"{JOUEUR.name}, Vous avez gagné !")
            break
        print(f"Le joueur attaque {atk} dégat. Le BOT lui reste {BOT.life} point de vie")
    if action == "2":
        print(f"Le joueur restaure : {JOUEUR.use_potion_of_life()} point de vie. Ce qui le fait {JOUEUR.life}")
    atk_bot = BOT.atk_player()
    JOUEUR.life -= atk_bot
    print(f"Le bot attaque {atk_bot} dégat. {JOUEUR.name} lui reste {JOUEUR.life if JOUEUR.life > 0 else 0} point de vie")
    print("_"*50)

if JOUEUR.life < 1:
    print(f"{JOUEUR.name}, Vous avez perdu !")