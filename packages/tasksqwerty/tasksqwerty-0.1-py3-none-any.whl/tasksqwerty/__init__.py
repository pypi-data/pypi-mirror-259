tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task deleted!")
    else:
        print("Task not found in the list.")

def update_task(old_task, new_task):
    if old_task in tasks:
        index = tasks.index(old_task)
        tasks[index] = new_task
        print("Task updated!")
    else:
        print("Task not found in the list.")

def display_tasks():
    if tasks:
        print("Tasks:")
        for task in tasks:
            print("- " + task)
    else:
        print("No tasks in the list.")

