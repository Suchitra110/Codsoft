class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"
class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added successfully.")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if title is not None:
                self.tasks[index].title = title
            if description is not None:
                self.tasks[index].description = description
            if completed is not None:
                self.tasks[index].completed = completed
            print("Task updated successfully.")
        else:
            print("Invalid task index.")
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")
def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to update: ")) - 1
                title = input("Enter new task title (leave blank to skip): ")
                description = input("Enter new task description (leave blank to skip): ")
                completed_input = input("Is the task completed? (yes/no/leave blank to skip): ").strip().lower()
                completed = None
                if completed_input == 'yes':
                    completed = True
                elif completed_input == 'no':
                    completed = False
                todo_list.update_task(index, title if title else None,
                                       description if description else None,
                                       completed)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            todo_list.view_tasks()
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()