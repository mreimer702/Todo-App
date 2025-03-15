# Options list
options = ["add tasks", "view tasks", "delete tasks", "quit the application"]

# Task storage
tasks = []

#Function to add a task
def add_task():
    try:
        adding = input("What task would you like to add? ").strip()
        if not adding:
            raise ValueError("Task cannot be empty.")
        else:
            tasks.append(adding)
            print(f"Task '{adding}' added successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Returning to the main menu...")
        print(f"\nYou can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

#Function to view a task
def view_tasks():
    try:
        if not tasks:
            raise ValueError("Your to-do list is empty. Add some tasks first.")
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Returning to the main menu...")
        print(f"\nYou can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

#Function to delete a task
def delete_task():
    try:
        if not tasks:
            raise ValueError("There are no tasks to delete.")
        
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

        deleting = input("Enter the exact task you want to delete: ").strip()
        if deleting not in tasks:
            raise ValueError("Task not found. Please enter a valid task from your list.")
        else:
            tasks.remove(deleting)
            print(f"Task '{deleting}' deleted successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Returning to the main menu...")
        print(f"\nYou can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

#Function to exit the application
def exit_app():
    print("See you next time!")
    exit()  # Terminates the script

# Main application loop
print(f"Welcome, visitors! On Martin Reimer's To-Do App, you can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

while True:
    try:
        task = input("\nWhat would you like to do now on Martin Reimer's To-Do App? ").strip().lower()

        if task == "add tasks":
            add_task()
        elif task == "view tasks":
            view_tasks()
        elif task == "delete tasks":
            delete_task()
        elif task == "quit the application":
            exit_app()
        else:
            raise ValueError("Invalid choice. Please select a valid option.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

