import pytest

@pytest.fixture()
def fixture_one():
    print("\nHey, this id fixture one!")
    yield
    print("\nBy from fixture one")

@pytest.fixture()
def fixture_two(fixture_one):
    print("\nHey, this id fixture two!")
    yield
    print("\nBy from fixture two")

def test_function(fixture_two):
    print("\nHey, I,m test function!")