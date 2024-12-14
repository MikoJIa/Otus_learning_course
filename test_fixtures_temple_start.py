import pytest

def test_one(first_fixture):
    print("test_one")


def test_two(first_fixture):
    print("test_two")


class TestFunction:

    @pytest.fixture
    def fixt(self):
        print("Fixture inside ClassFunction")

    def test_from_test_class_one(self, fixt, first_fixture):
        print("test_class_1")

    def test_from_test_class_two(self, first_fixture):
        print("test_class_2")