print("Hello, enter 3 numbers!")
number1 = int(input("Enter 1 number: "))
number2 = int(input("Enter 2 number: "))
number3 = int(input("Enter 3 number: "))

choice = input("Choose an action (max, min, avg): ")

if choice == "max":
    result = max(number1, number2, number3)
    print("Maximum: ", result)
elif choice == "min":
    result = min(number1, number2, number3)
    print("Minimal: ", result)
elif choice == "avg":
    result = (number1 + number2 + number3) / 3
    print("Arithmetic average: ", result)
else:
    print("Wrong question!")

