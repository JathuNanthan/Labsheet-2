cost_price = float(input("Enter the cost price (CP): "))
selling_price = float(input("Enter the selling price (SP): "))

profit_loss = selling_price - cost_price

if profit_loss > 0:
    print(f"There is a gain of Rs. {profit_loss:.2f}.")
elif profit_loss < 0:
    print(f"There is a loss of Rs. {-profit_loss:.2f}.")
else:
    print("There is neither gain nor loss. The item was sold at the cost price.")
