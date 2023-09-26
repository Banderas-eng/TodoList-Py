from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

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

#functions for menu items
def saveList():
    file = filedialog.asksaveasfilename(
    initialdir = "C:/Users/Yande/Desktop/Projects/Python_Projects", 
    title = "Save", filetypes = (("Dat Files", "*.dat"), ("All files", "*.*"))
    )
    
    if file:
        if file.endswith(".dat"):
            pass
        else:
            file = f'{file}.dat'

        things = my_list.get(0, END) #getting all things from the list

        fileOutput = open(file, "wb") #open selcted file wb means write binary

        pickle.dump(things, fileOutput)   #add things to the file you open in previous line

def openList():
    pass

def clearList():
    my_list.delete(0, END) #deletes everything from the list

#menu box created here
menuBox = Menu(root)
root.config(menu=menuBox)

menu_bar = Menu(menuBox, tearoff=False)
menuBox.add_cascade(label="File", menu=menu_bar)

#items on dropdown menu
menu_bar.add_command(label="Save", command=saveList)
menu_bar.add_command(label="Open", command=openList)
menu_bar.add_separator()
menu_bar.add_command(label="Clear All", command=clearList)
  

root.mainloop()
