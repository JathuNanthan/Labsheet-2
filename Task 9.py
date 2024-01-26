number = float(input("Enter a number: "))

if number < 0:
    print(f"{number} is a negative number.")
elif number > 0:
    print(f"{number} is a positive number.")
else:
    print(f"{number} is equal to zero.")
