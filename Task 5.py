start_reading = float(input("Enter the starting meter reading: "))
end_reading = float(input("Enter the ending meter reading: "))


units_consumed = end_reading - start_reading


if units_consumed > 200:
    rate = 3.50
elif units_consumed > 100:
    rate = 2.50
else:
    rate = 1.50

total_bill = units_consumed * rate


print(f"Units Consumed: {units_consumed} units")
print(f"Rate: Rs. {rate} per unit")
print(f"Total Bill: Rs. {total_bill}")
