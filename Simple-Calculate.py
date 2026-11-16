"""Simple Calculate"""

number_1 = float(input("Enter your first Number :- "))
number_2 = float(input("Enter your second Number :- "))

operator = input("Choose an operation (+,-,*,/) :- ")

if operator == "+":
    print(f"Total Addition: {number_1 + number_2}")
elif operator == "-":
    print(f"Total Subtraction: {number_1 - number_2}")
elif operator == "*":
    print(f"Total Multiplicatin: {number_1 * number_2}")
elif operator == "/":
    if number_2 == 0:
        print("Cannot divide by zero!")
    else:
        print(f"Total Division: {number_1 / number_2}")
else:
    print("Invalid operator!")