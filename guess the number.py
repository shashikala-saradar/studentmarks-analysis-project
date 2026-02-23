import random
# attempt=0
secret_number=random.randint(0,5)
print(secret_number)
while True:
    guess=int(input("enter any integer"))
    # attempt+=1
    if guess<secret_number:
        print("it is too low")
    elif guess>secret_number:
        print("it is  too high")
    else:
        print("congralitutaion😍")
        break

