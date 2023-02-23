#!/usr/bin/python3
from budget import Category
import pytest

food = None
entertainment = None
clothes = None
party = None


def setup_module(module):
    print('***SETUP***')
    global food, entertainment, clothes, party
    food = Category(food)
    entertainment = Category(entertainment)
    clothes = Category(clothes)
    party = Category(party)

def test_deposit():
    food.deposit(10.22, "Initial deposit")
    actual = food.ledger[0]
    expected = {"amount": 10.22, "description": "Initial deposit"}
    assert actual == expected

def test_deposit_no_description():
    entertainment.deposit(100)
    actual = entertainment.ledger[0]
    expected = {"amount": 100, "description": ""}
    assert actual == expected

def test_withdrawl():
    food.withdrawl(0.22, "gum")
    actual = food.ledger[1]
    expected = {"amount": -0.22, "description": "gum"}
    assert actual == expected

def test_witdrawl_not_funds():
    actual = food.withdrawl(30.21, "No funds")
    expected = False
    assert actual == expected

def test_withdrawl_not_description():
    entertainment.withdrawl(1)
    assert entertainment.ledger[1]["description"] == ''

def test_get_balance():
    actual = food.get_balance()
    expected = 10.00
    assert actual == expected

def test_transfer():
    actual = food.transfer(0.20, entertainment)
    expected = entertainment.get_balance() == 99.20
    assert actual == expected

def test_no_funds_transfer():
    actual = entertainment.transfer(12000, food)
    expected = False
    assert actual == expected

def test_check_funds():
    actual = food.check_funds(1)
    expected = True
    assert actual == expected
    actual = food.check_funds(10000)
    expected = False
    assert actual == expected
