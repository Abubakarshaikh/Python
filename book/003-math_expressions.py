# objective: match expresions
# 1. +, - * /
# 2. use of %
# 3. Increament and Decreament

print("First Number: ")
n1 = int(input())

print("second Number: ")
n2 = int(input())

print("Select Any one Operators, +, -, *, /, % ")
op = input()

if op == "+":
    print("The Addition is : ",n1 + n2)
elif op == "-":
    print("The Subtraction is: ",n1 - n2)
elif op == "*":
    print("The Multiply is: ",n1 * n2)
elif op == "/":
    print("The division is: ",n1 / n2)
elif op == "%":
    print("The Remainder is: ",n1 % n2)
else:
    print("Invalid Operator:")
