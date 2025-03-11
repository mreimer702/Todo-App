# Options list
options = ["add tasks", "view tasks", "delete tasks", "quit the application"]

# Task storage
tasks = []

print(f"Welcome, visitors! On Martin Reimer's To-Do App, you can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")

while True:
    try:
        task = input("What would you like to do now on Martin Reimer's To-Do App? ").strip().lower()

        if task == "add tasks":
            try:
                add = input("What task would you like to add? ").strip()
                tasks.append(add)
                print(f"Task '{add}' added successfully.")
            except ValueError:
                print("Task cannot be empty.")
            
        elif task == "view tasks":
            try:
                print("Your To-Do List:")
                for index, element in enumerate(tasks, start=1):
                    print(f"{index}. {element}")
            except ValueError:
                print("Your to-do list is empty. Add some tasks first.")
            

        elif task == "delete tasks":
            if len(tasks) == 0:
                raise ValueError("There are no tasks to delete.")
            print("Your To-Do List:")
            for index, element in enumerate(tasks, start=1):
                print(f"{index}. {element}")
            delete = input("Enter the task you want to delete: ").strip()
            if delete not in tasks:
                raise ValueError("Task not found. Please enter a valid task from your list.")
            tasks.remove(delete)
            print(f"Task '{delete}' deleted successfully.")

        elif task == "quit the application":
            print("See you next time!")
            break  # Exit the loop

        else:
            raise ValueError("Invalid choice. Please select a valid option.")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print(f"You can {options[0]}, {options[1]}, {options[2]}, or {options[3]}.")
