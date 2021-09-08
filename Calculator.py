# Store the user input of 2 numbers and the operator
num1, operand, num2 = input("Enter Calculation: ").split()

# Convert the strings into integer
num1 = int(num1)
num2 = int(num2)
# output is provided based on operator entered
if operand == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operand == "-":
    print("{} - {} = {}".format(num1, num2,  num1 - num2))
elif operand == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operand == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Use either of these operators -> +, -, *, /")