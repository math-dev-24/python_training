import re
import string
from tinydb import TinyDB, where, table
from pathlib import Path


class User:
    DB = TinyDB(Path(__file__).resolve().parent / "db.json", indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str = "", address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def db_instance(self) -> table.Document:
        return User.DB.get((where('first_name') == self.first_name) & (where("last_name") == self.last_name))

    # Quand on appelle l'object cela va afficher ça
    def __str__(self):
        return f" {self.full_name} \n {self.phone_number} \n {self.address} \n __________________"

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name}, {self.phone_number}, {self.address})"

    def _check_phone_number(self):
        phone_digit = re.sub(r"[+()\s]*", "", self.phone_number)
        if len(phone_digit) < 10 or not phone_digit.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    def _check_names(self):
        if not (self.first_name and self.last_name):
            raise ValueError('Le prénom et le nom de famille ne peuvent pas être vides.')
        special_characters = string.punctuation + string.digits
        # façon de faire débutant
        for character in self.first_name + self.last_name:
            if character in special_characters:
                raise ValueError(f"Nom invalide : {self.full_name}")

    def _check(self):
        self._check_names()
        self._check_phone_number()

    def exists(self) -> bool:
        return bool(self.db_instance)

    def delete(self) -> list[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def save(self, validate_data: bool = False) -> int:
        if validate_data:
            self._check()

        if self.exists():
            return -1
        else:
            # donne le dictionnaire de instance __dict__
            return User.DB.insert(self.__dict__)


def get_all_users():
    return [User(**user) for user in User.DB.all()]


if __name__ == "__main__":
    # récuperer toutes la data
    # print(get_all_user())

    # ___________ inserer de la data
    from faker import Faker
    # faker permet de générer des données fake
    # fake = Faker(locale="fr_FR")
    # par convention quand on utilise pas on met un _
    # for _ in range(4):
    # user = User(
    # first_name=fake.first_name(),
    # last_name=fake.last_name(),
    # phone_number=fake.phone_number(),
    # address=fake.address())
    # print(user.save(validate_data=True))

    # récuperer l'instance de la base de données
    # Martin_Camus = User(first_name="Martin",last_name="Camus")
    # print(Martin_Camus.delete())
