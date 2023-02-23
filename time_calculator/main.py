#/usr/bin/python3
from time_calculator import add_time
import pytest

if __name__=='__main__':
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
    # Run unit tests automatically
    pytest.main(['test_module.py', '--verbose'])
