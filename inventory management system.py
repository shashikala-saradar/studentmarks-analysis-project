inventory={
    "Store1":{"Rice":50,"Oil":30},
    "Store2":{"Rice":20,"Oil":10}

}
for store,products in inventory.items():
    print(store)
    for item,qty in products.items():
        print(item,":",qty)
    print()   