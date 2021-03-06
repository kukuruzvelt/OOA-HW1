import sys

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = ['+', '-']
checkedString = ""
inputString = ""


def is_formula(string, sign):  # determines if an expressions is a formula
    passed, checked_string = 0, ""
    for i in string:
        if i in numbers:
            if passed == 0:
                checked_string += sign
            checked_string += i
            passed += 1
        elif i in signs:
            if passed == 0 and sign:
                return [False, "None"]
            passed = passed + 1
            result = is_formula(string[passed:], i)
            if result[0]:
                checked_string = checked_string + result[1]
                return [True, checked_string]
            else:
                return [False, "None"]
        else:
            return [False, "None"]
    return [True, checked_string]


try:
    inputString = sys.argv[1]
    finalResult = is_formula(inputString, "")
    print("result:", finalResult[0], ",", eval(finalResult[1]))
except IndexError as ex:
    print("ERROR: no input")
