#!/usr/bin/python3
import budget
import pytest

food = budget.Category("Food")
food.deposit(2000, "initial deposit")
food.withdrawl(225, "week meal")
food.withdrawl(168.50, "delivery order")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(220, clothing)
clothing.withdrawl(122.25)
clothing.withdrawl(79.50)
bike = budget.Category("Bike")
bike.deposit(1112, "initial deposit")
bike.withdrawl(99.15)
sport = budget.Category("Sport")
bike.transfer(200, sport)
sport.withdrawl(500, "winter material for friends and family of other places")

print(food)
print(clothing)
print(bike)
print(sport)
print(budget.create_spend_chart([food, clothing, bike, sport]))

pytest.main(['test_module.py', '--verbose'])
