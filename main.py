print("*" * 15 ,"To-Do List", "*" * 15)
print("\n")

todo_list = []

title=""
desc = ""




def create_todo_list():
    
    while True:
        
   
       title = input("To-do List title : ")
       if title.lower() == "exit":
        break
    
       desc = input("Description : ")
       if desc.lower() == "exit":
        
           break
    
    todo_list.append({ "title":title, "description":desc})


create_todo_list()

print(todo_list)

for title in todo_list: 
    print(title["title"])