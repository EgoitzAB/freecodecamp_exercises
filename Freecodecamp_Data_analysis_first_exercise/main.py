#!/usr/bin/python3
import pytest
from mean_var_std import calculate

if __name__=='__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))
    pytest.main(['test_module.py', '--verbose'])
