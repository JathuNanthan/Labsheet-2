day_number = int(input("Enter a number (1-7) representing the day of the week: "))

if 1 <= day_number <= 7:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = days_of_week[day_number - 1]
    print(f"The day corresponding to {day_number} is {day_name}.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
