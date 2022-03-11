# Libraries
import pytest

# Functions
from fchecker import type_check


__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, test_type_checks'
__credits__ = ['IncognitoCoding']
__license__ = 'MIT'
__version__ = '0.1'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Development'


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_type_check():
    """
    Tests type check success.
    """
    type_check(value='mytest', required_type=str)


def test_1_1_type_check():
    """
    Tests type check success.
    """
    type_check(value=1, required_type=int)


def test_1_2_type_check():
    """
    Tests type check success.
    """
    type_check(value=1, required_type=[int, str])


def test_1_3_type_check():
    """
    Tests type check success.
    """
    msg_override = 'Incorrect (<Sample Key>) YAML value.'
    type_check(value=1, required_type=int, tb_remove_name=None, msg_override=msg_override)


# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_type_check():
    """
    Tests incorrect input issues.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(value=1, required_type={'key': 1})
    assert 'No type or list of types has been entered for type validation.' in str(excinfo.value)


def test_2_1_type_check():
    """
    Tests incorrect input issues.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(value=None, required_type=int)
    assert """The value 'None' sent is not an accepted input.""" in str(excinfo.value)


def test_2_2_type_check():
    """
    Tests incorrect input issues with msg_override.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(value=None, required_type=int, msg_override='The required employee data was not sent.')
    assert """The required employee data was not sent.""" in str(excinfo.value)


def test_2_3_type_check():
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(value=1, required_type=str)
    assert """The value '1' is not in <class 'str'> format""" in str(excinfo.value)


def test_2_4_type_check():
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        type_check(value=1, required_type=[str, bool])
    assert """The value '1' is not in [<class 'str'>, <class 'bool'>] format.""" in str(excinfo.value)


def test_2_5_type_check():
    """
    Tests type check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        msg_override = 'Incorrect (<Sample Key>) YAML value.'
        type_check(value=1, required_type=str, tb_remove_name=None, msg_override=msg_override)
    assert 'Incorrect (<Sample Key>) YAML value.' in str(excinfo.value)


def test_2_6_type_check():
    """
    Tests type check validation failure with traceback alteration.
    """
    with pytest.raises(Exception) as excinfo:
        msg_override = 'Incorrect (<Sample Key>) YAML value.'
        type_check(value=1, required_type=str, tb_remove_name='test_2_6_type_check', msg_override=msg_override)
    assert 'Incorrect (<Sample Key>) YAML value.' in str(excinfo.value)
    # If pytest updates there modules these outputs could change.
    assert """<class 'str'>""" in str(excinfo.value)
    assert """<class 'int'>""" in str(excinfo.value)
    assert """Module: python""" in str(excinfo.value)
    assert """Name: pytest_pyfunc_call""" in str(excinfo.value)
    assert """Line: 183""" in str(excinfo.value)
