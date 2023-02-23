#!/usr/bin/python3
class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        string = f"{self.name:*^30}\n"
        for item in self.ledger:
            string += f"{item['description'][0:23]:<23}" + f"{item['amount']:>7.2f}\n"
        string += "Total: " + f"{self.get_balance():.2f}"
        return string

    def deposit(self, amount, description=''):
        result = {'amount': amount, 'description': description}
        self.ledger.append(result)

    def withdrawl(self, amount, description=''):
        result = {'amount': - amount, 'description': description}
        if self.check_funds(amount):
            self.ledger.append(result)
            return True
        return False

    def get_balance(self):
        current_balance = 0
        for i in range(len(self.ledger)):
            current_balance += self.ledger[i]["amount"]
        return current_balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdrawl(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True


def create_spend_chart(categories):
    spent_amounts = []
    category_list = []
    for cat in categories:
        spent = 0
        category_list.append(cat.name)
        for i in cat.ledger:
            if i["amount"] < 0:
                spent += abs(i["amount"])
        spent_amounts.append(round(spent, 2))
    total_spent = round(sum(spent_amounts, 2))
    category_percentage = list(map((lambda amount: int(((amount / total_spent) * 10) // 1) * 10), spent_amounts))
    title = "Percentage spent by category\n"
    chart = ''
    for v in reversed(range(0, 101, 10)):
        chart += str(v).rjust(3) + '|'
        for percent in category_percentage:
            if percent >= v:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    bar = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    longest_str = max(category_list, key=len)
    longest_str_num = len(longest_str)
    for value in range(0, longest_str_num):
        bar += "    "
        number = 1
        for category in category_list:
            if len(category) > value:
                bar += (" " + category[value] + " ")
                if number == len(category_list):
                    bar += " "
            else:
                bar += "   "
            number += 1
        bar += "\n"
    bar = bar.rstrip()
    bar += "  "
    return title + chart + bar
