from tkinter import *
from tkinter.font import Font

root = Tk()

root.title("ToDoList")
root.geometry("400x400")

# two functions created
def add_item():
    my_list.insert(END, inputfield.get())
    inputfield.delete(0, END)

def delete_item():
    my_list.delete(ANCHOR)

label = Label(text="My-ToDo-List", font= "Georgia, 20 bold", width=10, bd=5, fg="red")
label.pack()

ft = Font(family="Blackadder ITC", size=30)

my_list = Listbox(width=20, height=4, bd=0, fg="#09143C", 
                  bg="SystemButtonFace", font=ft, selectbackground="grey", activestyle="none", highlightthickness=0)
my_list.pack()

#input section
#add task
inputfield = Entry(root, font=("Arial", 20))
inputfield.pack(pady=20)

        #buttons
addButton = Button(text="ADD", command=add_item)
deleteButton = Button(text="DELETE", command=delete_item)

addButton.place(x=130, y=320)
deleteButton.place(x=220, y=320)

#menu box created here
menuBox = Menu(root)
root.config(menu=menuBox)



stuff = ["walk", "train", "code"]
for items in stuff:
    my_list.insert(END, items)    

root.mainloop()