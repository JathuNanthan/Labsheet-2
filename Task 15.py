purchase_amount = float(input("Enter the purchase amount: "))

if purchase_amount > 5000:
    discount_percentage = 15
else:
    discount_percentage = 10

discount = (discount_percentage / 100) * purchase_amount
amount_to_pay = purchase_amount - discount

print(f"Purchase Amount: £{purchase_amount:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Discount Amount: £{discount:.2f}")
print(f"Amount to Pay: £{amount_to_pay:.2f}")
