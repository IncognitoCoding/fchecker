# Libraries
import pytest

# Functions
from fchecker import file_check

# Exception
from fexception import FFileNotFoundError

__author__ = 'IncognitoCoding'
__copyright__ = 'Copyright 2022, test_file_checks'
__credits__ = ['IncognitoCoding']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'IncognitoCoding'
__status__ = 'Beta'


# ############################################################
# ######Section Test Part 1 (Successful Value Checking)#######
# ############################################################


def test_1_file_check() -> None:
    """
    Tests file check success.
    """
    file_check(file_path='test_file_checks.py', file_description='test_file_checks')


# ############################################################
# ####Section Test Part 2 (Successful Exception Checking)#####
# ############################################################


def test_2_file_check() -> None:
    """
    Tests file validation failure with description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check(file_path='Bad File', file_description='test_file_checks')
    assert ('The file (test_file_checks) does not exist in the validating '
            'file path (Bad File).' in str(excinfo.value))


def test_2_1_file_check() -> None:
    """
    Tests file validation failure with out description.
    """
    with pytest.raises(Exception) as excinfo:
        file_check(file_path='Bad File')
    assert ('The file does not exist in the validating '
            'file path (Bad File).' in str(excinfo.value))
