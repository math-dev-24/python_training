from random import *

class User_game:
    def __init__(self, name):
        self.name = name
        self.point = 0
        self.tool_game = ["Pierre", "Ciseau", "Papier"]

    def random_tool(self):
        return self.tool_game[randint(0,2)]
    
    def add_point(self):
        self.point += 1

    def verif_win(self, j1, bot):
        # 0 : null
        # 1 : J1
        # 2 : Bot
        if j1 == self.tool_game[0]:
            if bot == self.tool_game[0]:
                return 0
            if bot == self.tool_game[1]:
                return 1
            if bot == self.tool_game[2]:
                return 2
        if j1 == self.tool_game[1]:
            if bot == self.tool_game[0]:
                return 2
            if bot == self.tool_game[1]:
                return 0
            if bot == self.tool_game[2]:
                return 1
        if j1 == self.tool_game[2]:
            if bot == self.tool_game[0]:
                return 1
            if bot == self.tool_game[1]:
                return 2
            if bot == self.tool_game[2]:
                return 0
