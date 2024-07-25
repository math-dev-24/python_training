# ____
from random import randint
# ____
from term_printer import Color, Format, cprint
from colorama import Fore
# ____
from constantes import TITLE, RULES, SQUARE, PASTILLE, Colors, DIFFICULTY


class Mastermind(Colors):
    def __init__(self):
        self.difficulty: str = ""
        self.target: list[int] = []
        self.user: list[int] = []
        self.indicators: list[Fore] = []
        self.done: bool = False
        self.attempts: int = 0
        self.max_attempts: int = 10
        self.win: bool = False

    def __call__(self):
        cprint(f"{TITLE}", attrs=[Color.BG_MAGENTA])
        print(RULES)
        self.game()

    def choice_difficulty(self):
        while self.difficulty not in DIFFICULTY:
            cprint("Choix de la difficulté : facile | normal", attrs=[Format.BOLD])
            self.difficulty = input("🎤️ > ").strip().lower()

    def game(self):
        self.choice_difficulty()
        self.print_all_colors()
        self.generate_random_combination()
        self.win = False
        while True:
            self.indicators = []
            self.user = []
            self.attempts += 1
            self.question()
            if not self.check():
                self.show_invalid_input_message()
            else:
                self.get_indicator()
                if self.done:
                    if self.win:
                        print(self.get_user_selection_text())
                        cprint(f"Vous avez gagné ! Bravo ! En {self.attempts} coups !", attrs=[Color.GREEN, Format.BOLD])
                    else:
                        cprint(f"Vous avez perdu !", attrs=[Color.RED, Format.BOLD])
                    break
                self.print_response()
        self.restart()

    def restart(self):
        cprint(f"Voulez-vous continuer ? Oui | Non", attrs=[Color.BG_MAGENTA, Format.UNDERLINE])
        if input('🎤️ > ').strip().lower() == "oui":
            self.game()
        else:
            cprint("Au revoir !!!", attrs=[Color.RED, Format.BOLD])
            exit()

    def generate_random_combination(self):
        self.target = []
        for _ in range(4):
            self.target.append(randint(1, 6))

    def question(self):
        print("\n Veuillez saisir vos quatre chiffres pour les couleurs :")
        self.user = [int(i) for i in input('🎤️ > ').strip() if i.isnumeric()]

    def check(self) -> bool:
        return len(self.user) == 4 and min(self.user) > 0 and max(self.user) < 7

    def get_indicator(self):
        red = Fore.RED
        white = Fore.WHITE
        count: int = 0
        tmp_target: list[int] = self.target.copy()
        for i in range(len(self.target)):

            if self.user[i] in self.target and self.user[i] != self.target[i] and self.user[i] in tmp_target:
                tmp_target.remove(self.user[i])
                self.indicators.append(white)

            elif self.user[i] == self.target[i] and self.user[i] in tmp_target:
                tmp_target.remove(self.user[i])
                self.indicators.append(red)
                count += 1

            else:
                self.indicators.append([])

        self.win = count == 4
        self.done = count == 4 or self.attempts == self.max_attempts

    def print_response(self):
        print(f"{self.get_user_selection_text()} - Indicateurs : {self.get_indicators_text()}")

    def get_user_selection_text(self):
        u_colors: list[Fore] = [self.COLORS[num - 1][1] for num in self.user]
        return ' '.join(self.print_color(SQUARE, color) for color in u_colors)

    def get_indicators_text(self):
        if self.difficulty == "facile":
            tmp = [ind if ind else Fore.BLACK for ind in self.indicators]
            return ' '.join(self.print_color(PASTILLE, color) for color in tmp)
        else:
            tmp = [ind for ind in self.indicators if ind]
            return ''.join(self.print_color(PASTILLE, color) for color in tmp)

    @staticmethod
    def show_invalid_input_message():
        cprint("Votre saisie est incorrecte...", attrs=[Color.RED])


if __name__ == "__main__":
    master = Mastermind()
    master()
