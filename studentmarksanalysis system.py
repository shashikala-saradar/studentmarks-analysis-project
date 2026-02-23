students={
    "ravi":[80,75,90],
    "Anu":[80,75,65]
}
for name,mark in students.items():
    total=0
    for m in mark:
        total+=m
    print(name,"total:",total)