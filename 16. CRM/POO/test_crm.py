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


def test__check_phone_number():
    assert False


def test__check_names():
    assert False


def test_exists():
    assert user.exists() is True


def test_not_exists(setup_db):
    user = User(first_name="test", last_name="test", address="20 route du vieux chateau",
                phone_number="0123456789")
    assert user.exists() is False


def test_save():
    assert False
