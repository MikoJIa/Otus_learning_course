import pytest


@pytest.fixture(scope="function")
def setup_function_fixture():
    print("\nHello fro setup function fixture!\n")
    yield
    print("\nBye bye from setup module fixture!\n")


@pytest.fixture(scope="module")
def setup_function_fixture():
    print("\nHello fro setup module fixture!\n")
    yield
    print("\nBye bye from setup module fixture!\n")

def test_one(setup_function_fixture):
    print("test one")


def test_two(setup_function_fixture):
    print("test two")