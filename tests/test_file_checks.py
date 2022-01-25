import pytest

# Methods or functions
from fchecker import file_check
# Exception classes
from fexception import FFileNotFoundError


# -------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------type_check pytests-----------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------

# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_file_check() -> None:
    """
    Tests file check success.
    """
    try:
        file_check('test_file_checks.py', 'test_file_checks')
    except FFileNotFoundError:
        pytest.fail("The file did not pass the validation check.")

# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_file_check() -> None:
    """
    Tests file validation failure with description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check('Bad File', 'test_file_checks')
    assert ('The file (test_file_checks) does not exist in the validating '
            'file path (Bad File).' in str(excinfo.value))


def test_2_1_file_check() -> None:
    """
    Tests file validation failure with out description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check('Bad File')
    assert ('The file does not exist in the validating '
            'file path (Bad File).' in str(excinfo.value))
