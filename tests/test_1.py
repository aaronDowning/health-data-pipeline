import pytest
from transforms import clean_name

def test_clean_name():
    assert clean_name("Aaron Badger") == "Aaron Badger";
    assert clean_name("aaron Badger") == "Aaron Badger";

