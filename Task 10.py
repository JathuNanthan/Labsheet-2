marks = float(input("Enter the marks: "))

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks <= 89:
    grade = "B"
elif 70 <= marks <= 79:
    grade = "C"
else:
    grade = "D"

print(f"Marks: {marks}")
print(f"Grade: {grade}")
