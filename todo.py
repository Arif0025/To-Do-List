import os

TODO_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("✔️ Task added!")
    else:
        print("❗ Task cannot be empty.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Removed: {removed}")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n---- TO-DO LIST MANAGER ----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
