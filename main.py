import os
from datetime import datetime

# Clear the screen function for cross-platform support
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Print title
print("*" * 15, "To-Do List", "*" * 15)
print("\n")

# Initialize to-do list
todo_list = []

def create_todo_item():
    """Add a new item to the to-do list."""
    while True:
        current_date = datetime.now()
        item_id = current_date.strftime("%Y%m%d%H%M%S")

        title = input("To-Do List Title (type 'exit' to stop adding): ")
        if title.lower() == "exit":
            break

        desc = input("Description: ")
        if desc.lower() == "exit":
            break

        todo_list.append({"id": item_id, "title": title, "description": desc})
        print("To-do item added successfully!\n")

def show_todo_list():
    """Display all items in the to-do list."""
    if not todo_list:
        print("No items in the to-do list.\n")
    else:
        print("\nYour To-Do List:\n")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. ID: {item['id']}")
            print(f"   Title: {item['title']}")
            print(f"   Description: {item['description']}\n")

def delete_todo_item():
    """Delete an item from the to-do list by index."""
    show_todo_list()
    if not todo_list:
        print("To-do list is empty.\n")
        return

    try:
        index = int(input("Enter the number of the item to delete: ")) - 1
        if 0 <= index < len(todo_list):
            deleted_item = todo_list.pop(index)
            print(f"Deleted '{deleted_item['title']}' successfully.")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def update_todo_item():
    """Update an item in the to-do list by index."""
    show_todo_list()
    if not todo_list:
        print("To-do list is empty.\n")
        return

    try:
        index = int(input("Enter the number of the item to update: ")) - 1
        if 0 <= index < len(todo_list):
            current_item = todo_list[index]
            print(f"Selected item to update: '{current_item['title']}'")

            new_title = input("New title (leave blank to keep current): ")
            new_desc = input("New description (leave blank to keep current): ")

            if new_title:
                current_item['title'] = new_title
            if new_desc:
                current_item['description'] = new_desc

            print("To-do item updated successfully!")
        else:
            print("Invalid number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main program loop
while True:
    clear_screen()
    print("1: Add To-Do Item")
    print("2: Show All To-Do Items")
    print("3: Delete To-Do Item")
    print("4: Update To-Do Item")
    print("5: Exit\n")

    choice = input("> ")

    if choice == "1":
        clear_screen()
        create_todo_item()
    elif choice == "2":
        clear_screen()
        show_todo_list()
        input("Press Enter to return to the main menu...")
    elif choice == "3":
        clear_screen()
        delete_todo_item()
        input("Press Enter to return to the main menu...")
    elif choice == "4":
        clear_screen()
        update_todo_item()
        input("Press Enter to return to the main menu...")
    elif choice == "5":
        clear_screen()
        print("Exiting...")
        break
    else:
        print("Invalid input, please try again.")
        input("Press Enter to continue...")

