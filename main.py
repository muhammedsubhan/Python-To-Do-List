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
 
     
     
    

while True:
    print("1: Add To-Do List \n")
    print("2: Show All To-Do Lists \n")
    print("3: Delete Todo List \n")
    
    print("4: Exit \n")

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
        print("Exiting...")
        break
    else:
        print("Invalid input, please try again.")
