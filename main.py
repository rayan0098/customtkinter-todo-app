import customtkinter as ctk

#screen 
ctk.set_appearance_mode("dark")
screen = ctk.CTk()
screen.geometry("600x400")
screen.title("TO-DO lists")

#title in the window
title = ctk.CTkLabel(master=screen, text="TO-DO", font=("Arial", 20))
title.pack(pady=20)

#entry in the window
entry = ctk.CTkEntry(master=screen, placeholder_text="Write your task here...",width=200)
entry.pack(pady=20)

#checkbox storage

check_boxes = []


#function for the button
def add_task():
    

    task = entry.get().strip()
    if task == "":
          return
    
    checkbox = ctk.CTkCheckBox(master=screen, text=task)
    checkbox.pack(pady=5)
    
    entry.delete(0, ctk.END)
    check_boxes.append(checkbox)

    
def delete_check_box():
    global check_boxes
    new_check_boxes = []
    
    
    for checkbox in check_boxes:
     if checkbox.get() == 1:
        checkbox.destroy()
     else:
        new_check_boxes.append(checkbox)   

    check_boxes = new_check_boxes 
     


#desyroy button in the window
delete_button = ctk.CTkButton(master=screen, text="DELETE",command=delete_check_box)
delete_button.pack(pady=20)


#add button in the window
button = ctk.CTkButton(master=screen, text="ADD",command=add_task)
button.pack(pady=20)



screen.mainloop()
