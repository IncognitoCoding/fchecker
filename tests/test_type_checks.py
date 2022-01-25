import pytest

# Methods or functions
from fchecker import type_check
# Exception classes
from fexception import FTypeError


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_type_check() -> None:
    """
    Tests type check success.
    """
    try:
        type_check('mytest', str)
    except FTypeError:
        pytest.fail("The type value did not pass the type validate check.")


def test_1_1_type_check() -> None:
    """
    Tests type check success.
    """
    try:
        type_check(1, int)
    except FTypeError:
        pytest.fail("The type value did not pass the type validate check.")


def test_1_2_type_check() -> None:
    """
    Tests type check success.
    """
    try:
        type_check(1, [int, str])
    except FTypeError:
        pytest.fail("The type value did not pass the type validate check.")


def test_1_3_type_check() -> None:
    """
    Tests type check success.
    """
    try:
        msg_override = 'Incorrect (<Sample Key>) YAML value.'
        type_check(1, int, None, msg_override=msg_override)
    except FTypeError:
        pytest.fail("The type value did not pass the type validate check.")

# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_type_check() -> None:
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(1, str)
    assert """The value '1' is not in <class 'str'> format""" in str(excinfo.value)


def test_2_1_type_check() -> None:
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(1, [str, bool])
    assert """The value '1' is not in [<class 'str'>, <class 'bool'>] format.""" in str(excinfo.value)


def test_2_2_type_check() -> None:
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        msg_override = 'Incorrect (<Sample Key>) YAML value.'
        type_check(1, str, None, msg_override=msg_override)
    assert 'Incorrect (<Sample Key>) YAML value.' in str(excinfo.value)


# ############################################################
# #######Section Test Part 3 (Incorrect Arg Exception)########
# ############################################################


def test_3_type_check():
    """
    Tests incorrect input issues.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(1, {'key': 1})
    assert 'No type or list of types has been entered for type validation.' in str(excinfo.value)


def test_3_1_type_check():
    """
    Tests incorrect input issues.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(None, int)
    assert """The value 'None' sent is not an accepted input.""" in str(excinfo.value)
