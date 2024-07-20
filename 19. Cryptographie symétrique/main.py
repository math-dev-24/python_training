TEXT: list[tuple[str, int, str]] = [
    ("Salut, je suis ici pour apprendre Python", 6, "S_i_adtajspprhle_opeou_iur_ntscreP*,ui_ny*"),
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 12,
     "Ldetnootugrl,r_eo__emrcal__odiisnitpisp.stei*u_cs*matc*_mei*"),
    ("La première machine programmable a été réalisé en 1801.", 3,
     "Lpmrmherrmlatrlén8.arieai_oaae_ééi__0*_eè_cnpgmb_é_ase11*")
]


def encode(sentence: str, key: int) -> str:
    sentence += "*" * (key - len(sentence) % key) if len(sentence) % key else ""
    return "".join(sentence[i::key] for i in range(key)).replace(" ", "_")


def decode(sentence_encrypt: str, key: int) -> str:
    cutter = len(sentence_encrypt) // key
    return "".join(sentence_encrypt[i::cutter] for i in range(cutter)).replace("_", " ").rstrip("*")


if __name__ == "__main__":
    code = TEXT[2]

    text: str = code[0]
    key: int = code[1]
    encode_str: str = code[2]

    check: bool = encode(text, key) == encode_str

    print(encode(text, key), "->", check)


    check: bool = decode(encode_str, key) == text
    print(decode(encode_str, key), "->", check)
