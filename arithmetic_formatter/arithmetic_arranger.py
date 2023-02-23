#!/usr/bin/python3

def arithmetic_arranger(operation, value=False):
    """Function who return formated values of one arithmetic operation"""
    result = []
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    if len(operation) > 5:
        return "Error: Too many problems"

    for element in operation:
        element = element.split()
        if element[1] != '+' and element[1] != '-':
            return "Error: Operator must be '+' or '-'"
        try:
            int(element[0]) and int(element[2])
        except:
            return "Error: Numbers must only contain digits."
        if (len(element[0]) > 4) or (len(element[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        if element[1] == "+":
             result = int(element[0]) + int(element[2])
        else:
            result = int(element[0]) - int(element[2])
        longest_operand = max(len(element[0]), len(element[2]))
        dashes = '-'
        case_separation = (len(element[0]) - len(element[2]) + 1) * ' '
        if (len(element[0]) > len(element[2])):
            line1 += str(f"{element[0]}".rjust(longest_operand + 2) +"    ")
            line2 += str(f"{element[1]}{case_separation}{element[2]}" + "    ")
            line3 += str((dashes * (len(element[0]) + 2) + "    "))
            line4 += str((str(result).rjust(longest_operand + 2) + "    "))
        else:
            line1 += str(f"{element[0]}".rjust(longest_operand + 2) +"    ")
            line2 += str(f"{element[1]} {element[2]}" + "    ")
            line3 += str(dashes * (longest_operand + 2) +"    ")
            line4 += str(str(result).rjust(longest_operand+2) + "    ")
    if value == True:
        return f"{line1}\n{line2}\n{line3}\n{line4}\n"
