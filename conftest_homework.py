import pytest


ls = [1, 2, 3, 4, 5, 6, 7, 8]
dic = {'a': 'cat', 'b': 'dog', 'c': 'rad'}
s = {1, 4, 6, 8, 9}

@pytest.fixture(scope="function")
def data_type_length():
    return len(ls)

@pytest.fixture()
def set_add_elements():
    s.add(9)
    return s

@pytest.fixture()
def set_occurrence_identical_elements():
    count = 0
    s.add(8)
    for i in s:
        s1 = s.copy()
        s1.remove(i)
        if i in s1:
            count += 1
        count = count
    return count

@pytest.fixture()
def dictionary_add_keys():
    dic['d'] = 'elephant'
    return dic

@pytest.fixture()
def data_append():
    ls.append(1)
    return ls

@pytest.fixture()
def data_remove():
    ls.remove(5)
    return ls

@pytest.fixture()
def data_type():
    return type(ls)


class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_plus(self, a, b):
        return a + b

    def calc_minus(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a

@pytest.fixture(scope="class")
def return_calc_res():
    return Calculator(a=5, b=6)
