import pytest


@pytest.fixture(scope="function")
def setup_function_fixture():
    print("\n Hello from setup function fixture")
    yield
    print("\nBye bye from setup function fixture!")


@pytest.fixture(scope="module")
def setup_function_fixture():
    print("\n Hello from setup module fixture")
    yield
    print("\nBye bye from setup module fixture!")

def test_one(setup_function_fixture):
    print("one test")

def test_two(setup_function_fixture):
    print("test two")