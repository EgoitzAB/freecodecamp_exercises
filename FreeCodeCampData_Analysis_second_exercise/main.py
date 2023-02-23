#!/usr/bin/python3
import pytest
from demographic_data_analyzer import demographic_analyzer

if __name__=='__main__':
    print(demographic_analyzer())
    pytest.main(['test_module.py', '--verbose'])
