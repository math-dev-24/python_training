from term_printer import Color, Format, cprint, StdText
from random import randint

TITLE: str = "JEU DU MASTERMIND"

RULES: str = """Trouver la bonne combinaison des quatre couleurs sectrètes !
2 modes de jeu :
normal : 
    Règle classique : 
    * A chaque couleur bien positionnée, vous aurez en retour un indicateur rouge.
    * A chaque couleur présent mais mal positionnée, vous auez en retour un indicateur blanc.
    * les pastilles indique juste la présence ou bon positionnement de la couleur.
easy : 
    Les indicateurs sont positionnés en face de la couleur.
    * Même code couleur que le mode normal.
    * La couleur noir correspond à une couleur non présente.
    
"""

SQUARE: str = "\u25A0"
PASTILLE: str = "\u25CF"

COLOR: list[list[str | Color]] = [
    ['Jaune', Color.YELLOW],
    ['Blue', Color.BLUE],
    ['Rouge', Color.RED],
    ['Vert', Color.GREEN],
    ['Blanc', Color.WHITE],
    ['Magenta', Color.MAGENTA]
]
DIFFICULTY: list[str] = ["easy", "normal"]


class Mastermind:
    def __init__(self):
        self.difficulty: str = ""
        self.target: list[int] = []
        self.user: list[int] = []
        self.indicators: list[list[str | Color]] = []
        self.done: bool = False
        self.attempts: int = 0

    def __call__(self, *args, **kwargs):
        cprint(f"{TITLE}", attrs=[Color.BG_MAGENTA])
        print(RULES)

        self.generate_random_combination()

        while self.difficulty not in DIFFICULTY:
            cprint("Choix de la difficulté : easy | normal", attrs=[Format.BOLD])
            self.difficulty = input("🎤️ > ").strip()
        self.print_available_colors()
        if self.difficulty == "easy":
            self.eay_mode()
        else:
            self.normal_mode()

    def normal_mode(self):
        pass

    def eay_mode(self):
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
                    cprint(f"Vous avez gagné ! Bravo ! En {self.attempts} coups !", attrs=[Color.GREEN, Format.BOLD])
                    break
                self.print_user_selection()
                self.print_indicators()

    def generate_random_combination(self):
        for _ in range(4):
            self.target.append(randint(1, 6))

    def question(self):
        cprint("\n Veuillez saisir vos quatre chiffres pour les couleurs !", attrs=[Format.UNDERLINE])
        self.user = [int(i) for i in input('🎤️ > ').strip() if i.isnumeric()]

    def check(self) -> bool:
        return len(self.user) == 4 and min(self.user) > 0 and max(self.user) < 7

    def get_indicator(self):
        red = COLOR[2]
        white = COLOR[4]
        count: int = 0
        for i in range(len(self.target)):
            # présent mais mal positionné
            if self.user[i] in self.target and self.user[i] != self.target[i]:
                self.indicators.append(white)
            # présent et bien positionné
            elif self.user[i] == self.target[i]:
                self.indicators.append(red)
                count += 1
            # pas présent
            else:
                self.indicators.append([])

        # gestion fin du jeu ?
        self.done = count == 4

    def print_user_selection(self):
        selected_colors = [COLOR[num - 1][1] for num in self.user]
        cprint(
            f"Votre choix : {StdText(SQUARE, selected_colors[0])} {StdText(SQUARE, selected_colors[1])} "
            f"{StdText(SQUARE, selected_colors[2])} {StdText(SQUARE, selected_colors[3])}")

    def print_indicators(self):
        tmp = [ind[1] if ind else Color.BLACK for ind in self.indicators]
        cprint(
            f"Indicateur :  {StdText(PASTILLE, tmp[0])} {StdText(PASTILLE, tmp[1])} "
            f"{StdText(PASTILLE, tmp[2])} {StdText(PASTILLE, tmp[3])}"
        )

    @staticmethod
    def print_available_colors():
        color_list_label: list[str] = [f"[{i + 1}]{color[0]}" for i, color in enumerate(COLOR)]
        print("   ".join(color_list_label))

    @staticmethod
    def show_invalid_input_message():
        cprint("Votre saisie est incorrecte...", attrs=[Color.RED])


if __name__ == "__main__":
    master = Mastermind()
    master()
