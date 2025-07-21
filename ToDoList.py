print("To do Menu List application --> ")

toDoList = []

def addToDoList(task):
    toDoList.append(task)

def removeFromDoList(task_number):
    if len(toDoList) == 0:
        print("No task to remove")
    try:
        toDoList.pop(task_number -1)
    except IndexError:
        print("Index out of range")

    print("Task removed")

def printToDoList():
    if len(toDoList) == 0:
        print("List is empty")
    for i, task in enumerate(toDoList,1):
        print(i, task)


menu =["1 - Add Task", "2 - Remove Task ", "3 - View Task","4 - Exit"]



while True:
    try:
        print("Choose option ", menu)
        choice = input("Enter your choice: ", )

        if choice == '1':
            addTask = input("Enter Task Name: ")
            addToDoList(addTask)
        elif choice == '2':
            tasknumber = int(input("Item to remove: "))
            try:
                removeFromDoList(tasknumber)
            except:
                print("supply valid number")
        elif choice == '3':
            print("Here are the list of tasks:")
            printToDoList()
        elif choice == '4':
            break
        else:
            print("Invalid choice")
    except:
        print("Something went wrong")
