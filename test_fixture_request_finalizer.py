import pytest


@pytest.fixture()
def first_fixture_for_request(request):

    def fin():
        print("\n This is finalizer from first_fixture_for_request")
    request.addfinalizer(fin)


def test_one(first_fixture_for_request):
    print("One test")