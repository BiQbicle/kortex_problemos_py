tasks = []

def addTask():
    task = input("Enter task: ")
    tasks.append([task, False])

def viewTasks():
    if len(tasks) == 0:
        print("Yayyyyy we free (for now)")
    else:
        i = 1
        for t in tasks:
            if t[1] == True:
                status = "✔"
            else:
                status = "✘"
            print(str(i) + ". " + t[0] + " [" + status + "]")
            i += 1

def completeTask():
    viewTasks()
    num = input("Enter task number to complete: ")
    if num.isdigit():
        num = int(num)
        if num > 0 and num <= len(tasks):
            tasks[num-1][1] = True
        else:
            print("Input a valid number ya dimwit")
    else:
        print("Invalid input ya retard!")
def removeTask():
    viewTasks()
    num = input("Enter the task number to delete: ")
    if num.isdigit():
        num = int(num)
        if num > 0 and num <= len(tasks):
            tasks[num-1][1] = True            
            tasks.pop(num)
        else:
            print("Invalid input dumbahh")
    

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Remove Task\n5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        addTask()
    elif choice == "2":
        viewTasks()
    elif choice == "3":
        completeTask()
    elif choice == "4":
        removeTask()
    elif choice == "5":
        break
    else:
        print("Invalid choice ya Retard!")
