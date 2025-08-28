# Load existing items
# 1. create a new item
# 2. list the items
# 3. complete the item
# 4. save an item
import json

file_name = 'todo_list.json'

def display_task(task):
    print("Description: ",task["description"])
    status = '[Completed]' if task["complete"] else '[Pending]'
    print("Status: ", status)

def load_tasks():
    
    try:
        with open(file_name, 'r') as f:
           return json.load(f)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    
    try:
        with open(file_name, 'w') as f:
            json.dump(tasks, f)
    except:
        print("Failed to save")

def view_tasks(tasks):
    print()
    tasks_list = tasks["tasks"]

    if len(tasks_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: \n")
        for index, task in enumerate(tasks_list, start=1):
            status = '[Completed]' if task["complete"] else '[Pending]'
            print(f'Task {index}. {task['description']} |  {status}')

def create_task(tasks):
    description = input("Enter your task description: ").strip()

    if description:
        tasks["tasks"].append({"description":description, "complete":False})
        save_tasks(tasks=tasks)
        print("Task added")
    else:
        print("Task description cannot be an empty.")

def mark_task_complete(tasks):
    view_tasks(tasks=tasks)
    
    try:
        task_number = int(input("Enter the taks number to mark as complete: ").strip())

        if 1 <= task_number <= len(tasks):
            tasks['tasks'][task_number-1]['complete'] = True
            save_tasks(tasks=tasks)
            print(f'Task {task_number} marked as complete.')
        else:
          print("Invalid Task number.")
    except:
        print("Please enter valid number.")



def main():
    
    tasks = load_tasks()


    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            view_tasks(tasks=tasks)
        elif choice == '2':
            create_task(tasks=tasks)
        elif choice == '3':
            mark_task_complete(tasks=tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try later again.")
            break



if __name__ == '__main__':
    
    main()
