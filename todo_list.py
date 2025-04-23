import os 

def display_menu():
    print("===========To-Do-List===========")
    print("1. Add tasks")
    print("2. View Tasks")
    print("3. Mark as done")
    print("4. Exit")
    
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added succesfully! NOw complete that damn task already")
    
def view_tasks(tasks):
    print("\nTasks: ")
    for i, task in enumerate(tasks, start = 1):
        print(f"{i}. {task}")   
    
def mark_task_done(tasks):
    if not tasks:
        print("Dayum you've been productive.")
        return
    
    view_tasks(tasks)
    index = int(input("Enter task number (the number before task) to mark as complete: ")) - 1
    
    if 0 <= index < len(tasks):
         removed_task = tasks.pop(index)
         print(f"Task '{removed_task}' marked as done and removed yayyyyyyyy.")
    else:
        print("Invalid task index.")
    
def main():
    tasks = []  


    while True:
        display_menu()


        choice = input("Enter your choice already: ")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Enter a valid choice you dumbass ._.")


if __name__ == "__main__":
    main()
