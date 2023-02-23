#!/usr/bin/python3
from arithmetic_arranger import arithmetic_arranger
import pytest

if __name__=='__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "9999 + 9998"], True))
    pytest.main(['test_module.py', '--verbose'])
