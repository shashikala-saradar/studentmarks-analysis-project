data=[101,102,103,101,104,102]
duplicates=[]
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]==data[j] and data[i] not in duplicates:
            duplicates.append(data[i])
print("Duplicate Records:",duplicates)


#common elements between two list
a=[1,2,3]
b=[1,2,3,4,5]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)