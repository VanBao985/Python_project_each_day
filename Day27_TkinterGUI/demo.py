import tkinter as tk

window = tk.Tk()
window.minsize(width=500, height=500)
window.title("My tkiner GUI program")


#Label
mylable = tk.Label(text="My label", font=("Courier", 20))
mylable.pack()

#pack() --> place(x=.., y=..): put label in coor (x,y)
#pack() --> grid(column=.., row=.., columnspan=..): devide layout to column*row squares

#Button
def button_clicked():
    #get input from entry
    new_text = myentry.get()

    mylable.config(text=new_text)

#call action() when press
mybutton = tk.Button(text="Click me", command=button_clicked)
mybutton.pack()

#Entry
myentry = tk.Entry(width=25)
#add something with...
myentry.insert(tk.END, string="Insert something: ...")
myentry.pack()


#Text
text = tk.Text(width=25, height=8)
#custom cursor in text
text.focus()
#add something with ...
text.insert(tk.END, "Insert...")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.pack()

#Spin box
def spinbox_used():
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to=100, command=spinbox_used)
spinbox.pack()

#Scale
#print current value scale
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Check button
def checkbutton_used():
    print(checked_state.get())

#variable to hold on to checked state: 0 is off, 1 is on
checked_state = tk.IntVar()
check_button = tk.Checkbutton(text="Is on?", command=checkbutton_used, variable=checked_state)
checked_state.get()
check_button.pack()

#Radio Button
def radiobutton_used():
    print(radiobutton_state.get())

radiobutton_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option 1", value=1, command=radiobutton_used, variable=radiobutton_state)
radiobutton2 = tk.Radiobutton(text="Option 2", value=2, command=radiobutton_used, variable=radiobutton_state)
radiobutton1.pack()
radiobutton2.pack()


#List box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=3)
fruits = ["apple", "banana", "orrange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
    
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()