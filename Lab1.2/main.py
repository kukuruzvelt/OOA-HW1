import sys

action = sys.argv[1]
firstNum = sys.argv[2]
secondNum = sys.argv[3]
str = "int(" + firstNum + ").__" + action + "__(int(" + secondNum + "))"
print(eval(str))
