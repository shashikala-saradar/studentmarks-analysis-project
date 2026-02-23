rent=int(input("enter total rent"))
foodorderd=int(input("enter foodorderd rent"))
electricity=int(input("enter electricity rent"))
charge_per_unit=int(input("enter charg_per _unitl rent"))
n=int(input("enter no of student "))
total_bill=(rent+foodorderd+electricity+charge_per_unit)//n
print(f"each person will pay {total_bill}")

