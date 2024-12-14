import pytest

# Сначало про scope

# @pytest.fixture(autouse=True)
# def function_fixture(request):
#     print(f"\n Hello from {request.scope} fixture!")
#     def fin():
#         print(f"\n Finalize from {request.scope} fixture!")
#     request.addfinalizer(fin)
#
#
# @pytest.fixture(scope="class", autouse=True)
# def class_fixture(request):
#     print(f"\n Hello from {request.scope} fixture!")
#
#     def fin():
#         print(f"\n Finalize from {request.scope} fixture!")
#     request.addfinalizer(fin)


# @pytest.fixture(scope="module", autouse=True)
# def module_fixture(request):
#     print(f"\nHello from {request.scope} fixture!")
#
#     def fin():
#         print(f"\n Finalize from {request.scope} fixture!")
#     request.addfinalizer(fin)
#
# @pytest.fixture(scope="session", autouse=True)
# def session_fixture(request):
#     print(f"\n Hello from {request.scope.upper()} fixture!")
#     def fin():
#         print(f"\n Finalize from {request.scope.upper()} fixture!")
#     request.addfinalizer(fin)

def test_one():
    print(">>> i'm test one")


def test_two():
    print(">>> i'm test two")


class TestClass():

    def test_one(self):
        print("Test_in_class_1")

    def test_two(self):
        print("Test_in_class_2")