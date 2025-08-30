import os
# Nate all Higgers! (joke)
tasks = []
if os.path.exists("list.txt"):
    f = open("list.txt", "r")
    lines = f.readlines()
    for line in lines:
        stuff = line.strip().split(" | ")
        if len(stuff) == 2:
            if stuff[1] == "True":
                tasks.append([stuff[0], True])
            else:
                tasks.append([stuff[0], False])
    f.close()

def addTask(): 
    task = input("Enter task: ")
    tasks.append([task, False])
    f = open("list.txt", "a")
    f.write(task + " | False\n")
    f.close()

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
            f = open("list.txt", "w")
            for t in tasks:
                f.write(t[0] + " | " + str(t[1]) + "\n")
            f.close()
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
            tasks.pop(num-1)
            f = open("list.txt", "w")
            for t in tasks:
                f.write(t[0] + " | " + str(t[1]) + "\n")
            f.close()
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
