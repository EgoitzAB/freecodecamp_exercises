#!/usr/bin/python3
import copy
import random
from collections import Counter

class Hat:

    def __init__(self, **kwargs):
        self.contents = [color for color, number in kwargs.items() for _ in range(number)]

    def draw(self, quantity):
        """ Function who makes a random choice for given parameters in a class"""
        balls = []
        contents = self.contents
        if quantity < len(self.contents):
            for x in range(quantity):
                ball = random.choice(self.contents)
                balls.append(ball)
                self.contents.remove(ball)
            return balls
        else:
            contents = self.contents
            self.contents = []
            return contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """ Function who makes experiment extracting balls from a hat and comparing
    with the expected balls to return the number of times that it happens."""
    try:
        m = 0
        for _ in range(0, num_experiments):
            hat_exp = copy.deepcopy(hat)
            expected_res = [ball for ball, number in expected_balls.items() for _ in range(number)]
            result = hat_exp.draw(num_balls_drawn)
            count = Counter(expected_res)
            count_res = Counter(result)
            intersection = count & count_res
            if count == intersection:
                m += 1
            else:
                continue
        return m / num_experiments
    except ZeroDivisionError:
        return 0
