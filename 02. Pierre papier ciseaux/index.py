from random import *
from user import User_game

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
            tool_j1 = joueur.tool_game[tool_tour]
            point = joueur.verif_win(tool_j1, tool_bot)
            
            if point == 1: 
                joueur.add_point
                print(f'{joueur.name} : {tool_j1} VS {bot.name} : {tool_bot} \n +1 point pour {joueur.name} ce qui fait {joueur.point}')
            if point == 2: 
                bot.add_point
                print(f'{joueur.name} : {tool_j1} VS {bot.name} : {tool_bot} \n +1 point pour {bot.name} ce qui fait {bot.point}')
            if point == 0:
                print('Match Nul')

        else:
            print('Hors plage')
            pass
    else:
        print('Veuillez rentrer un nombre ! \n -------------------------------------')
        pass
    print('--------------------------')

if bot.point == max_point:
    print(f'{bot.name} à remporté le match')
if joueur.point == max_point:
    print(f'Vous avez remporté le combat {joueur.bot}')










