print("Hello, enter the number of meters!")
number = int(input("How many meters: "))

choice = input("What to translate (mile, inch, yard): ")

if choice == "mile":
     result = (number) * 0.00062137
     print("Mile: ", result)
elif choice == "inch":
     result = (number) * 39.37
     print("Inch: ", result)
elif choice == "yard":
     result = (number) * 1.0936
     print("Yard: ", result)
else:
     print("Wrong question!")

