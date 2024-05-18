#Planner!
#make a to-do
#mark a to-do
#time slots for each task
#priorities

# Create a way to store todos
todos = []

["clean", "laundry", "dog"]

# Create a function to print the todolist
def print_todos():
    i = 1
    for todo in todos:  
        print(f'{i}: {todo}')
        i += 1

# Create a function to add todos
def add_todo():
    print_todos()
    taskName = input("Please enter task: ")
    todos.append(taskName)
    print(f'{taskName} has been added to To-do list. UwU')
    print_todos()
print("Let's make your day productive!")
print_todos()

# Create a function to remove a todo by 'id
def remove_todo():
    print_todos()
    removeTask = int(input("Which task number do you want to remove? "))
    todos.pop(removeTask - 1)
    print_todos()
    

# Create a variable to see if the user is finished
finished = False
while finished != True:
    # Give user 'menu' options
    choice = input("Press 1 to add new task\nPress 2 to remove task\nPress 3 to view all tasks\nPress X to exit\n")
    
    # if choice is 'X' then allow user to add task
    if choice.lower() == 'x':
        finished = True

    # if choice is '1' then allow user to add task
    if choice == '1':
        add_todo()

    # if choice is '2' then allow user to remove a task
    if choice == '2':
        remove_todo()
    
    # if choice is '3' then allow user to view all tasks
    if choice == '3':
        print_todos()
        



    