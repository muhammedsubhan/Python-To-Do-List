import os
from datetime import datetime

print("*" * 15, "To-Do List", "*" * 15)
print("\n")

todo_list = []

def create_todo_list():
    
   
    
    while True:
        
        
         current_date = datetime.now()
    
         id = current_date.strftime("%Y%m%d%H%M%S")
    
        
         title = input("To-do List title (type 'exit' to stop adding): ")
         if title.lower() == "exit":
            break
        
         desc = input("Description: ")
         if desc.lower() == "exit":
            break
        
         todo_list.append({"id":id,"title": title, "description": desc})
    print("To-do item(s) added successfully!\n")

def show_todo_list():
    if not todo_list:
        print("No items in the to-do list. \n")
    else:
        print("\nYour To-Do List: \n ")
        for item in todo_list:
            print(f"id: {item['id']}")
            print(f"Title: {item['title']}")
            print(f"Description: {item['description']}\n")
            
            
def delete_todo_items():
    show_todo_list()
    
    if not todo_list:
        print("Todo list is empty...! \n")
    
    
    index = int(input("Enter choice to delete the Todo List : ")) - 1
    deleted_item  = todo_list.pop(index)
    
    print(f"{deleted_item['title']} is deleted Permanently")
 


def update_todo_list():
    show_todo_list()
    
    if not todo_list:
        print("Todo list is empty...! \n")
        
    index = int(input("Enter choice to update the Todo List : ")) - 1
    
    current_item = todo_list[index]
    
    print(f"selected item to update is : ({current_item['title']})")
    
    new_title = input("update the title (leave blank not to update title) : ")
    new_desc = input("update the description (leave blank not to update description) : ")
    
    if new_title:
        current_item['title'] = new_title
        
    if new_desc:
        current_item['description'] = new_desc
        
    print("To-do item updated successfully!")
    
    
    
    

     
    

while True:
    print("1: Add To-Do List \n")
    print("2: Show All To-Do Lists \n")
    print("3: Delete Todo List \n")
    print("4: Update Existing List \n")
    print("5: Exit \n")

    choice = input("> ")

    if choice == "1":
        os.system("cls")
        create_todo_list()
    elif choice == "2":
        os.system("cls")
        show_todo_list()
    elif choice == "3":
        os.system("cls")
        delete_todo_items()
    elif choice == "4":
        os.system("cls")
        update_todo_list()
    elif choice == "5":
        os.system("cls")
        print("Exiting...")
        break
    else:
        print("Invalid input, please try again.")
