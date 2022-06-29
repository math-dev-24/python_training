from random import *
from user import User_game

tool_game = ["Pierre","Ciseau","Papier"]


def verif_win(j1, bot):
    # 0 : null
    # 1 : J1
    # 2 : Bot
    match j1:
        case "Pierre":
            if bot == tool_game[0]:
                return 0
            if bot == tool_game[1]:
                return 1
            if bot == tool_game[2]:
                return 2
        case "Ciseau":
            if bot == tool_game[0]:
                return 2
            if bot == tool_game[1]:
                return 0
            if bot == tool_game[2]:
                return 1
        case "Papier":
            if bot == tool_game[0]:
                return 1
            if bot == tool_game[1]:
                return 2
            if bot == tool_game[2]:
                return 0



player = ""
max_point = 0
tour = 1

while player == "":
    player = str(input("Quel est votre pseudo ? >"))

while  max_point < 1:
        max = input("En Combien de point ? >")
        if max.isnumeric():
            max_point = int(max)

#Initialisation des joueurs
bot = User_game("bot")
joueur = User_game(player)

while bot.point != max_point or bot.point != max_point:
    print(f'Tour {tour} :')
    tool_tour = input('A vous de jouer : \n 0 : Pierre \n 1 : Ciseau \n 2 : Papier \n > ')
    if tool_tour.isnumeric():
        tool_tour = int(tool_tour)
        if tool_tour > 0 or tool_tour < 2:
            tool_bot = bot.random_tool
            tool_j1 = tool_game[tool_tour]
            point = verif_win(tool_j1,tool_bot)
            if point == 1:
                joueur.point += 1
                print(f'{joueur.name} : {tool_j1} VS {bot.name} : {tool_bot} \n +1 point pour {joueur.name} ce qui fait {joueur.point}')
            if point == 2:
                bot.point += 1
                print(f'{joueur.name} : {tool_j1} VS {bot.name} : {tool_bot} \n +1 point pour {bot.name} ce qui fait {bot.point}')
        else:
            print('Hors plage')
            pass
    else:
        print('Veuillez rentrer un nombre !')
        pass

if bot.point == max_point:
    print(f'{bot.name} à remporté le match')
if joueur.point == max_point:
    print(f'Vous avez remporté le combat {joueur.bot}')










