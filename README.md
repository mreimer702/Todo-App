# Martin Reimer's To-Do App

## Description
Martin Reimer's To-Do App is a simple command-line application that allows users to manage their tasks efficiently. Users can add tasks, view their task list, delete tasks, and quit the application.

## Features
- **Add Tasks**: Users can add tasks to their to-do list.
- **View Tasks**: Users can view all their pending tasks.
- **Delete Tasks**: Users can remove specific tasks from the list.
- **Error Handling**: Proper error handling is implemented to alert users about invalid inputs and prevent unexpected crashes.

## Technologies Used
- Python 3

## How to Run the Application
1. Ensure you have Python installed on your computer.
2. Download the `main.py` file (or copy the code into a new Python file).
3. Open a terminal or command prompt and navigate to the directory containing the file.
4. Run the application using the command:
   ```sh
   python main.py
   ```
5. Follow the prompts to interact with the to-do list.

## Usage Instructions
1. When prompted, enter one of the available options:
   - `add tasks` to add a new task.
   - `view tasks` to display all tasks.
   - `delete tasks` to remove a task.
   - `quit the application` to exit the program.
2. Follow the on-screen instructions to manage your to-do list.
3. If you enter an invalid option, an error message will be displayed, and you will be prompted again.

## Error Handling
- If you try to add an empty task, the app will prompt you to enter a valid task.
- If you try to view tasks when the list is empty, an alert will inform you.
- If you attempt to delete a task that does not exist, the app will notify you.
- If you enter an invalid command, you will be asked to choose a valid option.

## Future Improvements
- Save tasks to a file so they persist after the program is closed.
- Add a graphical user interface (GUI) for better usability.
- Implement categories or priority levels for tasks.
