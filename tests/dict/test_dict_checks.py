# Libraries
import pytest

# Methods
from fchecker.dict import KeyCheck


__author__ = "IncognitoCoding"
__copyright__ = "Copyright 2022, test_dict_checks"
__credits__ = ["IncognitoCoding"]
__license__ = "MIT"
__version__ = "0.0.3"
__maintainer__ = "IncognitoCoding"
__status__ = "Beta"


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_keycheck() -> None:
    """
    Tests key check success.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
    check = key_check.all_keys(required_keys=("key1", "key3"))
    assert True is check


def test_1_2_keycheck() -> None:
    """
    Tests key check success.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
    key_check.contains_keys(required_keys=("key1"))


def test_1_1_reverse_keycheck() -> None:
    """
    Tests key check success.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
    key_check.contains_keys(required_keys="key1", reverse_output=True)


def test_1_2_reverse_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
    key_check.all_keys(required_keys=("key1", "key3"), reverse_output=True)


def test_1_3_reverse_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
    key_check.contains_keys(required_keys=("key1"), reverse_output=True)


def test_1_4_reverse_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={1: "value1", 2: "value2"})
    key_check.contains_keys(required_keys=2, reverse_output=True)


def test_1_5_reverse_keycheck() -> None:
    """
    Tests key check success in reverse.
    """
    key_check = KeyCheck(values={1: "value1", 2: "value2"})
    key_check.contains_keys(required_keys=(2), reverse_output=True)


# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_keycheck():
    """
    Tests missing key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.all_keys(required_keys=("Yellow", "Blue"))
    assert "The input keys have inconsistent value and requirement keys." in str(excinfo.value)


def test_2_1_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None})
        key_check.contains_keys(required_keys=("Yellow", "Blue", "Blue"))
    assert "The required key tuple contains duplicate keys. All keys must be unique." in str(excinfo.value)
    assert "Required Key(s) = ('Yellow', 'Blue', 'Blue')" in str(excinfo.value)


def test_2_2_keycheck():
    """
    Tests incorrect type input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None}, enforce={"Bad Type"})  # type: ignore
        key_check.contains_keys(required_keys="Green")  # type: ignore
    assert """The object value '{'Bad Type'}' is not an instance of the required class(es) or subclass(es).""" in str(
        excinfo.value
    )
    assert """<class 'bool'>""" in str(excinfo.value)
    assert """<class 'set'>""" in str(excinfo.value)


def test_2_3_keycheck():
    """
    Tests incorrect type input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None})
        key_check.contains_keys(required_keys={"Bad Type"})  # type: ignore
    assert """The required dictionary key(s) (required_keys) must be immutable data types.""" in str(excinfo.value)
    assert """<class 'int'> | <class 'float'> | <class 'bool'> | <class 'str'> | <class 'tuple'>""" in str(
        excinfo.value
    )
    assert """<class 'set'>""" in str(excinfo.value)


def test_2_4_keycheck():
    """
    Tests incorrect type input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None})
        key_check.all_keys(required_keys={"Bad Type"})  # type: ignore
    assert """The required dictionary key(s) (required_keys) must be immutable data types.""" in str(excinfo.value)
    assert """<class 'int'> | <class 'float'> | <class 'bool'> | <class 'str'> | <class 'tuple'>""" in str(
        excinfo.value
    )
    assert """<class 'set'>""" in str(excinfo.value)


def test_2_5_keycheck():
    """
    Tests no key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.all_keys(required_keys=())
    assert "No key(s) were sent" in str(excinfo.value)
    assert """Expected Key(s) = ()""" in str(excinfo.value)


def test_2_6_keycheck():
    """
    Tests no key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.contains_keys(required_keys=())
    assert "No key(s) were sent" in str(excinfo.value)
    assert """Expected Match Option Key(s) = ('Green', 'Blue', 'Red')""" in str(excinfo.value)


def test_2_7_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.all_keys(required_keys=("Yellow", "Blue", "Blue"))
    assert "The required key tuple contains duplicate keys. All keys must be unique." in str(excinfo.value)


def test_2_8_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={1: None, 2: None, 3: None})
        key_check.all_keys(required_keys=(2, 6, 7))
    assert """The dictionary key ('6') does not exist in the expected required key(s).""" in str(excinfo.value)
    assert """Expected Key(s) = (2, 6, 7)""" in str(excinfo.value)
    assert """Failed Key(s) = (1, 2, 3)""" in str(excinfo.value)


def test_2_9_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
        key_check.all_keys(required_keys=("key1", "key2"))
    assert """The dictionary key ('key2') does not exist in the expected required key(s).""" in str(excinfo.value)
    assert """Expected Key(s) = ('key1', 'key2')""" in str(excinfo.value)
    assert """Failed Key(s) = ('key1', 'key3')""" in str(excinfo.value)


def test_2_10_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"key2": "value1", "key3": "value2"})
        key_check.contains_keys(required_keys=("key5"))
    assert """Match Option Key(s) = 'key5'""" in str(excinfo.value)


def test_2_11_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
        key_check.all_keys(required_keys=("key1", "key2"))
    assert """Expected Key(s) = ('key1', 'key2')""" in str(excinfo.value)


def test_2_12_keycheck():
    """
    Tests key check validation failure. Checks with enforcement disabled.
    """
    key_check = KeyCheck(values={"key1": "value1", "key3": "value2"}, enforce=False)
    check = key_check.all_keys(required_keys=("key1", "key2"))
    assert False is check


def test_2_1_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.contains_keys(required_keys=("Yellow", "Blue", "Blue"), reverse_output=True)
    assert "The required key tuple contains duplicate keys. All keys must be unique." in str(excinfo.value)


def test_2_2_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.all_keys(required_keys=(), reverse_output=True)
    assert "No key(s) were sent" in str(excinfo.value)
    assert """Expected Key(s) = ('Green', 'Blue', 'Red')""" in str(excinfo.value)


def test_2_3_reverse_keycheck():
    """
    Tests duplicate key input issues.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Red": None})
        key_check.all_keys(required_keys="Red", reverse_output=True)
    assert "The input keys have inconsistent value and requirement keys." in str(excinfo.value)
    assert """Required Key(s) = ('Green', 'Blue', 'Red')""" in str(excinfo.value)


def test_2_4_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"key1": "value1", "key3": "value2"})
        key_check.all_keys(required_keys=("key1", "key2"), reverse_output=True)
    assert """Expected Key(s) = ('key1', 'key3')""" in str(excinfo.value)


def test_2_5_reverse_keycheck():
    """
    Tests reverse key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None})
        key_check.contains_keys(required_keys=("Yellow", "Blue"), reverse_output=True)
    assert """Match Option Key(s) = ('Green', 'Blue')""" in str(excinfo.value)


def test_2_6_reverse_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={"Green": None, "Blue": None, "Green": None})
        key_check.contains_keys(required_keys=("Blue", "Purple"), reverse_output=True)
    assert """Match Option Key(s) = ('Green', 'Blue')""" in str(excinfo.value)
    assert """Failed Key(s) = ('Blue', 'Purple')""" in str(excinfo.value)


def test_2_7_reverse_keycheck():
    """
    Tests key check validation failure.
    """
    with pytest.raises(Exception) as excinfo:
        key_check = KeyCheck(values={1: None, 2: None, 3: None})
        key_check.contains_keys(required_keys=(2, "Purple"), reverse_output=True)
    assert """Match Option Key(s) = (1, 2, 3)""" in str(excinfo.value)
    assert """Failed Key(s) = (2, 'Purple')""" in str(excinfo.value)


def test_2_8_reverse_keycheck():
    """
    Tests key check validation failure. Checks with enforcement disabled.
    """
    key_check = KeyCheck(values={1: None, 2: None, 3: None}, enforce=False)
    check = key_check.contains_keys(required_keys=(2, "Purple"), reverse_output=True)
    assert False is check
