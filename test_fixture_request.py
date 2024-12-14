import pytest


@pytest.fixture(scope="function")
def first_fixture_for_request(request):
    print(30 * "_")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print(12 * "_")
    # print("\n Request object data: ")
    # for el in list(dir(request)):
    #     print(el)

def test_one(first_fixture_for_request):
    print("\nPrint from 'test_one'")

# class TestClass:
#
#     def test_two(self, first_fixture_for_request):
#         print("\nPrint from 'test_two'")
#
#     def test_three(self, first_fixture_for_request):
#         print("\nPrint from 'test_three'")