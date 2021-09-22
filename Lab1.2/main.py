import sys

action = sys.argv[1]
firstNum = sys.argv[2]
secondNum = sys.argv[3]
str = "int(" + firstNum + ").__" + action + "__(int(" + secondNum + "))"
try:
    print(eval(str))
except ZeroDivisionError as ex:
    print("ERROR: division by 0")
except NameError as ex:
    print("ERROR: wrong input")
except AttributeError as ex:
    print("ERROR: wrong operation")
