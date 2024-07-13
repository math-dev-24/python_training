from typing import List, Tuple

DEVISE_MEXICAINE: List[Tuple[float, str]] = [
    (1000, "billete 1000 pesos"),
    (500, "billete 500 pesos"),
    (200, "billete 200 pesos"),
    (100, "billete 100 pesos"),
    (50, "billete 50 pesos"),
    (20, "billete 20 pesos"),
    (10, "moneda 10 pesos"),
    (5, "moneda 5 pesos"),
    (2, "moneda 2 pesos"),
    (1, "moneda 1 peso"),
    (0.5, "moneda 50 centavos"),
    (0.2, "moneda 20 centavos"),
    (0.1, "moneda 10 centavos"),
]


def decomposition(money: float) -> str:
    table: List[Tuple[str, int]] = []
    for value, name in DEVISE_MEXICAINE:
        count: int = int(money // value)
        if count:
            table.append((name, count))
            money = round(money - value * count, 2)

    response = "\n".join(f"{txt}: {count}" for txt, count in table)
    return response


if __name__ == "__main__":
    print(decomposition(147.8))
