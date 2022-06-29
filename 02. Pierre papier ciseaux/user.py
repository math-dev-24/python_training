from random import *

class User_game:
    def __init__(self, name):
        self.name = name
        self.point = 0

    def random_tool(self, tool_game):
        return tool_game[randint(0,2)]
    
    def add_point(self):
        self.point += 1

