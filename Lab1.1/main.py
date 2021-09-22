import sys

firstNum = sys.argv[1]
action = sys.argv[2]
secondNum = sys.argv[3]
try:
    print(eval(firstNum + action + secondNum))
except ZeroDivisionError as ex:
    print("ERROR: division by 0")
except NameError as ex:
    print("ERROR: wrong input")
except SyntaxError as ex:
    print("ERROR: wrong operation")
