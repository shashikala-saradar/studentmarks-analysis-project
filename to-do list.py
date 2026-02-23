tasks=[]
def show_tasks():
    print("\n Your tasks")
    for i,task in enumerate(tasks):
        print(i,"-",task)
while True:
    choice=input("enter ur choice(1-5)")
    if choice=='1':
        task=input("enter ur task")
        tasks.append(task)
    elif choice=='2':
        task_no=int(input("enter task number to remove"))
        tasks.pop(task_no)                    #remove tasks at specified position.
    elif choice=='3':
        show_tasks()
    elif choice=='4':
        break
    else:
        print("invalid choice")
print(tasks)

