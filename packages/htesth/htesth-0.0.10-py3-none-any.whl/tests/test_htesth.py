import pytest

from src.htesth import htest

def test_htest():
    assert 3 == htest(1, 2)