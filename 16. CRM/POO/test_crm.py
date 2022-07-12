from crm import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage


@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)


@pytest.fixture
def user(setup_db):
    user = User(first_name="Patrick", last_name="Martin", address="20 route du vieux chateau",
                phone_number="0123456789")
    user.save()
    return user


def test_first_name(user):
    assert user.first_name == "Patrick"


def test_full_name(user):
    assert user.full_name == "Patrick Martin"


def test_delete(user):
    assert False


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance['first_name'] == "Patrick"
    assert user.db_instance['last_name'] == "Martin"
    assert user.db_instance['address'] == "20 route du vieux chateau"
    assert user.db_instance['phone_number'] == "0123456789"


def test_no_db_instance(setup_db):
    user = User(first_name="test", last_name="test", address="20 route du vieux chateau",
                phone_number="0123456789")
    assert user.db_instance is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Patrick", last_name="Martin", address="20 route du vieux chateau",
                phone_number="0123456789")
    user_bad = User(first_name="Patrick", last_name="Martin", address="20 route du vieux chateau",
                phone_number="adzd")
    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()
    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_names_empty(setup_db):
    user_no_name = User(first_name="", last_name="", address="20 route du vieux chateau",
                phone_number="0123456789")

    with pytest.raises(ValueError) as err:
        user_no_name._check_names()
    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)

def test__check_names_invalid_character(setup_db):
    user_no_name = User(first_name="Pat_24", last_name="test23", address="20 route du vieux chateau",
                phone_number="0123456789")

    with pytest.raises(ValueError) as err:
        user_no_name._check_names()
    assert "Nom invalide" in str(err.value)


def test_exists():
    assert user.exists() is True


def test_not_exists(setup_db):
    user = User(first_name="test", last_name="test", address="20 route du vieux chateau",
                phone_number="0123456789")
    assert user.exists() is False


def test_save():
    assert False
