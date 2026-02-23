# balance=1000
# print("1.Deposit 2.withdraw 3.Check balance 4.Exit ")
# amount=100

# while True:
#     ch=int(input("enter ur choice"))
#     if ch==1:
#         deposit=int(input("enter an amount to be deposited"))
#         balance+=deposit
#         print(balance)
#     elif ch==2:
#         withdraw=int(input("enter an amount to be withdraw"))
#         if withdraw>balance:
#             print("insufficient funds")
#         balance-=withdraw
#         print(balance)
#     elif ch==3:
#         print(f"checked balance is {balance}")
#     elif ch==4:
#         print("exit")
#         break

# print(f"total balance is {balance}")

# balance=1000
# print("1.Deposit 2.withdraw 3.Check balance 4.Exit ")
# def deposit():
#     global balance
#     deposit_amount=int(input("enter an amount to be deposited"))
#     balance+=deposit_amount
#     print(balance)
# def withdraw():
#     global balance
#     withdraw_amount=int(input("enter an amount to be deposited"))
#     balance-=withdraw_amount
#     print(balance)
# while True:
#     choice=int(input("enter ur chooice:"))
#     if choice==1:
#         deposit()
#     elif choice==2:
#         withdraw()
#     elif choice==3:
#         cm=input("if u want to withdaw and deposit again choice 3(y/n):")
#         if cm=='n':
#             print(f"balanced amount is {balance}")
#         else:
#             print("choice 3 already executed"  )
            
#     else:
#         print("exit")
#         break
# print(f"total remained amount is {balance}")

corrected_pin="1234"
balance=1000
attempts=3
while attempts>0:
    pin=input("Enter your ATM PIN:")
    if pin==corrected_pin:
        print("😍Login successfull")
        break
    else:
        attempts-=1
        print("Invalid PIN,Attempts.attempts left=",attempts)
if attempts==0:
    print("Card blocked.Try again later.")
else:
    while True:
        print("ATM menu")
        print("1.Check balance")
        choice=input("enter ur choice")
        if choice=='1':
            print("your balance is",balance)
        elif choice=='2':
            amount=int(input("enter an deposit amount"))
            if amount>0:
                balance+=amount
                print("deposit succesfull")
            else:
                print("invalid amount")
        elif choice=='3':
            amount=int(input("Enter an amount to withdraw"))
            if amount>balance:
                print("in sufficient funds")
            else:
                balance-=amount
        elif choice=='4':
            print("Thank u for using the ATM")
            break
        else:
            print("Invalid choice.pleae try again")
print(balance)

    
