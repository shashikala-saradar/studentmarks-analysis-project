print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?"))
tips_a=int(input("How much tip would u like to give?10,12,or 15"))
splitting=int(input("how many people to split the bill"))
total_bill_to_be_payed=(total_bill+tips_a)/splitting
print(f"Each person should pay {total_bill_to_be_payed:.3f}")
