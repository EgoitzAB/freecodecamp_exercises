#!/usr/bin/python3
import pytest
from polygon_area import Rectangle, Square

a = None
b = None
c = None
d = None

def setup_module(module):
    global a, b, c, d
    a = Rectangle(4, 3)
    b = Rectangle(8, 6)
    c = Square(6)
    d = Square(4)

def test_rectangle_set_width():
    actual = a.set_width(5)
    assert a.width == 5

def test_square_set_width():
    actual = c.set_width(5)
    assert c.width == c.height

def test_rectangle_set_height():
    actual = a.set_height(4)
    assert a.height == 4

def test_square_set_height():
    actual = c.set_width(5)
    assert c.width == c.height

def test_set_side():
    actual = d.set_side(5)
    assert d.width, d.height == 5

def test_rectangle_get_area():
    actual = a.get_area()
    expected = 20
    assert actual == expected

def test_square_get_area():
    actual = c.get_area()
    expected = 25
    assert actual == expected

def test_rectangle_get_perimeter():
    actual = a.get_perimeter()
    expected = 18
    assert actual == expected

def test_square_get_perimeter():
    actual = c.get_perimeter()
    expected = 20
    assert actual == expected

def test_rectangle_get_diagonal():
    actual= b.get_diagonal()
    expected = 10
    assert actual == expected

def test_square_get_diagonal():
    actual = c.get_diagonal()
    expected = 7.0710678118654755
    assert actual == expected

def test_rectangle_picture():
    actual = a.get_picture()
    expected = ('*****\n*****\n*****\n*****\n')
    assert actual == expected

def test_square_picture():
    actual = c.get_picture()
    expected = ('*****\n*****\n*****\n*****\n*****\n')
    assert actual == expected

def test_get_amount():
    sh = Rectangle(1, 1)
    actual = a.get_amount_inside(sh)
    expected = 20
    assert actual == expected

def test_rectangle_string():
    actual = str(a)
    expected = "Rectangle(width=5, height=4)"
    assert actual == expected

def test_square_string():
    actual = str(c)
    expected = "Square(side=5)"
    assert actual == expected
