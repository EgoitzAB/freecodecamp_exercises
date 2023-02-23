#!/usr/bin/python3

import probability_calculator as pb
import pytest

def main():
    hat = pb.Hat(black=6, red=4, green=3)
    probability = pb.experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
    return probability




if __name__ == '__main__':
    print(main())
    pytest.main(['test_module.py', '--verbose'])
