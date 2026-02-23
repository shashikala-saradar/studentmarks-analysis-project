# print("welcome to our restaurant.Here's the menu:")
# d={'pizza': 45,
#    'pasta':50,
#    'Coffe':89,
#    'salad':67
# }
# print("pizza:rs45\npasta:rs50\ncoffe:rs89\nsalad:67")
# total=0
# order1=input("enter ur first item you want to order=")
# if order1 in d:
#    print(f"order of {order1} has been added")
#    total+=d[order1]
# else:
#    print("order something new")

# a=input("do u want to order anything else(y/N):")
# if a=='y':
#    another=input("enter another item:")
#    if another in d:
#       print(f"order of {another} has been added")
#       total+=d[another]
# else:
#    print("it's not here.Thank upasta")
# print(total)

print("welcome to our restaurant.Here's the menu:")
d={'pizza': 45,
   'pasta':50,
   'Coffe':89,
   'salad':67
}
print("pizza:rs45\npasta:rs50\ncoffe:rs89\nsalad:67")
total=0

order1=input("enter the first item to ordeer")
if order1 in d:
   total+=d[order1]
else:
   print("see onece menu")

while True:
   orders=input("enter item u want to take:")
   s=input("u want to continue(y/n)")
   
   if orders in d:
      total+=d[orders]
   elif s=='n':
      print("it's ok!..over")
      break

print(total)

   

