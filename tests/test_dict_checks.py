import pytest

# Methods or functions
from fchecker import KeyCheck
# Exception classes
from fchecker import InvalidKeyError


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_keycheck() -> None:
    """
    Tests key check success.
    """
    try:
        key_check = KeyCheck({'key1': 'value1', 'key3': 'value2'})
        key_check.all_keys(['key1', 'key3'])
    except InvalidKeyError:
        pytest.fail("The dictionary did not pass the key validation check.")


def test_1_2_keycheck() -> None:
    """
    Tests key check success.
    """
    try:
        key_check = KeyCheck({'key1': 'value1', 'key3': 'value2'})
        key_check.contains_keys(['key1'])
    except Exception:
        pytest.fail("The dictionary did not pass the key validation check.")

# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_keycheck() -> None:
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck({'key1': 'value1', 'key3': 'value2'})
        key_check.all_keys(['key1', 'key2'])
    assert """Expected Key(s) = ['key1', 'key2']""" in str(excinfo.value)
    assert 'Exception: InvalidKeyError' in str(excinfo.value)


def test_2_1_keycheck() -> None:
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck({'key2': 'value1', 'key3': 'value2'})
        key_check.contains_keys(['key5'])
    assert """Match Option Key(s) = ['key5']""" in str(excinfo.value)


def test_2_2_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck({'key1': 'value1', 'key3': 'value2'})
        key_check.all_keys(['key1', 'key2'])
    assert """Expected Key(s) = ['key1', 'key2']""" in str(excinfo.value)


def test_2_3_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck({'key1': 'value1', 'key3': 'value2'})
        key_check.all_keys(['key1', 'key2'], reverse_output=True)
    assert """Expected Key(s) = ['key1', 'key3']""" in str(excinfo.value)


def test_2_4_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        match_dict_key = {'Green': None, 'Blue': None, 'Green': None}
        key_check = KeyCheck(match_dict_key)
        key_check.contains_keys(['Yellow', 'Blue'], reverse_output=True)
    assert """Match Option Key(s) = ['Green', 'Blue']""" in str(excinfo.value)


# ############################################################
# #######Section Test Part 3 (Incorrect Arg Exception)########
# ############################################################


def test_3_keycheck():
    """
    Tests missing key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        match_dict_key = {'Green': None, 'Blue': None, 'Red': None}
        key_check = KeyCheck(match_dict_key)
        key_check.all_keys(['Yellow', 'Blue'])
    assert 'The input keys have inconsistent value and requirement keys.' in str(excinfo.value)


def test_3_1_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        match_dict_key = {'Green': None, 'Blue': None, 'Green': None}
        key_check = KeyCheck(match_dict_key)
        key_check.contains_keys(['Yellow', 'Blue', 'Blue'])
    assert 'The required key list contains duplicate keys. All keys must be unique.' in str(excinfo.value)


def test_3_2_keycheck():
    """
    Tests incorrect type input issues.
    """
    with pytest.raises(Exception) as excinfo:
        match_dict_key = {'Green': None, 'Blue': None, 'Green': None}
        key_check = KeyCheck(match_dict_key)
        key_check.contains_keys({'Bad Type'})
    assert """The value '{'Bad Type'}' is not in [<class 'str'>, <class 'list'>] format.""" in str(excinfo.value)
    assert 'Module: test_dict_checks' in str(excinfo.value)
    assert 'Name: test_3_2_keycheck' in str(excinfo.value)


def test_3_3_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        match_dict_key = {'Green': None, 'Blue': None, 'Red': None}
        key_check = KeyCheck(match_dict_key)
        key_check.contains_keys(['Yellow', 'Blue', 'Blue'], reverse_output=True)
    assert 'The required key list contains duplicate keys. All keys must be unique.' in str(excinfo.value)
