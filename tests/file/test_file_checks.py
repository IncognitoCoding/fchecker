# Libraries
import pytest
import os

# Functions
from fchecker.file import file_check


__author__ = "IncognitoCoding"
__copyright__ = "Copyright 2022, test_file_checks"
__credits__ = ["IncognitoCoding"]
__license__ = "MIT"
__version__ = "0.0.2"
__maintainer__ = "IncognitoCoding"
__status__ = "Beta"


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_file_check() -> None:
    """
    Tests file check success.
    """
    # Gets the parent root directory.
    preset_root_directory = os.path.dirname(os.path.realpath(__file__))
    file_check(file_path=f"{preset_root_directory}\\test_file_checks.py", file_description="test_file_checks")


# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_file_check() -> None:
    """
    Tests file validation failure with description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check(file_path="Bad File", file_description="test_file_checks")
    assert "The file (test_file_checks) does not exist in the validating " "file path (Bad File)." in str(excinfo.value)


def test_2_1_file_check() -> None:
    """
    Tests file validation failure without description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check(file_path="Bad File")
    assert "The file does not exist in the validating " "file path (Bad File)." in str(excinfo.value)


def test_2_2_file_check() -> None:
    """
    Tests file validation failure. Checks with enforcement disabled.
    """
    check = file_check(file_path="Bad File", file_description="test_file_checks", enforce=False)
    assert False is check
