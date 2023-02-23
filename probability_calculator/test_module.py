#!/usr/bin/python3
import pytest
import probability_calculator as pb

def test_is_list():
    hat1 = pb.Hat(yellow=2, red=1)
    actual = hat1.contents
    assert isinstance(actual, list)

def test_is_list_of_strings():
    hat1 = pb.Hat(yellow=2, red=1)
    actual = hat1.contents
    assert filter(lambda x : x == type(string), actual)

def test_hat_colors_name_times_in_list():
    hat1 = pb.Hat(yellow=3)
    actual = hat1.contents
    expected = ["yellow", "yellow", "yellow"]
    assert actual == expected

def test_draw_return_list():
    hat1 = pb.Hat(yellow=2, red=1)
    actual = hat1.draw(3)
    assert isinstance(actual, list)

def test_draw_return_list_of_strings():
    hat1 = pb.Hat(yellow=2, red=1)
    actual = hat1.draw(3)
    assert filter(lambda x : x == type(string), actual)

def test_draw_more():
    hat = pb.Hat(blue=1, yellow=1)
    actual = hat.draw(4)
    expected = ['blue', 'yellow']
    assert actual == expected

def test_draw_normal():
    hat = pb.Hat(blue=4)
    actual = hat.draw(3)
    expected = ['blue','blue','blue']
    assert actual == expected

def test_draw_non_return():
    hat = pb.Hat(blue=4)
    hat.draw(3)
    actual = hat.contents
    expected = ['blue']
    assert actual == expected

def test_draw_non_return_1():
    hat = pb.Hat(blue=4)
    hat.draw(4)
    actual = hat.contents
    expected = []
    assert actual == expected

def test_experiment_all_success_one_color():
    hat1 = pb.Hat(blue=4)
    actual = pb.experiment(hat=hat1, expected_balls={'blue':2}, num_balls_drawn=2, num_experiments=100)
    expected = 1.0
    assert actual == expected

def test_experiment_all_success_two_colors():
    hat1 = pb.Hat(blue=2, yellow=2)
    actual = pb.experiment(hat=hat1, expected_balls={'yellow': 2, 'blue':2}, num_balls_drawn=4, num_experiments=100)
    expected = 1.0
    assert actual == expected

def test_experiment_all_failed_one_color():
    hat1 = pb.Hat(blue=2)
    actual = pb.experiment(hat=hat1, expected_balls={'red': 2}, num_balls_drawn=2, num_experiments=100)
    expected = 0.0
    assert actual == expected

def test_experiment_all_failed_two_colors():
    hat1 = pb.Hat(blue=2, yellow=2)
    actual = pb.experiment(hat=hat1, expected_balls={'red': 1, 'white':1}, num_balls_drawn=2, num_experiments=100)
    expected = 0.0
    assert actual == expected

def test_experiment_middle_result():
    hat1 = pb.Hat(blue=2, yellow=2)
    actual =pb.experiment(hat=hat1, expected_balls={'blue': 1, 'yellow': 1}, num_balls_drawn=2, num_experiments=100)
    expected = 0.0
    expected_1 = 1.0
    assert actual != expected and actual != expected_1
