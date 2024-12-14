from conftest_homework import data_type_length, data_type, return_calc_res, data_append, data_remove, dictionary_add_keys, set_add_elements, set_occurrence_identical_elements


def test_dictionary_add(dictionary_add_keys):
    assert dictionary_add_keys['d'] == 'elephant'

def test_set_add(set_add_elements):
    assert 9 in set_add_elements


def test_set_identical_elements(set_occurrence_identical_elements):
    assert set_occurrence_identical_elements == 0


def test_data_type_length(data_type_length):
    assert data_type_length == 8


def test_data_type(data_type):
    assert data_type == list


def test_dta_append(data_append):
    assert len(data_append) == 9

def test_data_remove(data_remove):
    assert 5 not in data_remove

def test_class_calculator_plus(return_calc_res):
    assert return_calc_res.calc_plus(5, 6) == 11
    assert return_calc_res.calc_plus(10, 10) == 20



def test_class_calculator_minus(return_calc_res):
    assert return_calc_res.calc_minus(5, 6) == 1
    assert return_calc_res.calc_minus(10, 20) == 10
