speed = int(input("Enter the speed in mph: "))

if 31 <= speed <= 40:
    fine = 50
elif 41 <= speed <= 50:
    fine = 75
elif speed > 50:
    fine = 100
else:
    fine = 0

if fine > 0:
    print(f"Fine for speeding at {speed} mph: £{fine}")
else:
    print("No fine for this speed.")
