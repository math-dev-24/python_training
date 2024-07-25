from colorama import Fore, Style

# title
TITLE: str = "JEU DU MASTERMIND"

# rules
RULES: str = """Trouver la bonne combinaison des quatre couleurs sectrètes en moins de 10 tentatives !
2 modes de jeu :
normal : 
    Règle classique : 
    * A chaque couleur bien positionnée, vous aurez en retour un indicateur rouge.
    * A chaque couleur présent mais mal positionnée, vous auez en retour un indicateur blanc.
    * les pastilles indique juste la présence ou bon positionnement de la couleur, elle n'indique pas le positionnement.
easy : 
    Les indicateurs indique le positionnement de la couleur.
    * Même code couleur que le mode normal.
    * La couleur noir correspond à une couleur non présente.
"""

# items
SQUARE: str = "\u25A0"
PASTILLE: str = "\u25CF"

# difficulty
DIFFICULTY: list[str] = ["facile", "normal"]


# colors
class Colors:
    COLORS: list[tuple[str, str]] = [
        ("jaune", Fore.YELLOW),
        ("bleu", Fore.BLUE),
        ("rouge", Fore.RED),
        ("vert", Fore.GREEN),
        ("blanc", Fore.WHITE),
        ("magenta", Fore.MAGENTA)
    ]

    @staticmethod
    def print_color(text: str, color: str) -> str:
        return f"{color}{text}{Style.RESET_ALL}"

    def print_all_colors(self):
        print("   ".join(self.print_color(f"{i + 1}. {color[0]}", color[1]) for i, color in enumerate(self.COLORS)))
