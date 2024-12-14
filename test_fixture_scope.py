def test_one(function_fixture, class_fixture, module_fixture, session_fixture):
    print("test_one")


def test_two(function_fixture, class_fixture, module_fixture, session_fixture):
    print("test_two")

class TestClass:
    def test_one(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("test_one_class")

    def test_two(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("test_two_class")

    def test_three(self, function_fixture, class_fixture, module_fixture, session_fixture):
        print("test_three_class")