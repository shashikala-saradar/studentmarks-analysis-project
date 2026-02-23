import random


choice=input("enter ur choice to droa a dice")
attempt=0
while True:
    choice2=input("do u want to paly another time(y/n)")
    attempt+=1
    if choice2=='y':
        print(random.randint(1,6))
        print("u got correct number")

    else:
        print("Invalid entry")
        break
    