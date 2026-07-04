from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)


# Label
my_lable = Label(text = "I am a Label", font=("Arial", 24, "bold"))
my_lable.pack()

my_lable["text"] = "NewText"
my_lable.config(text = "New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text=new_text)

button = Button(text="Click Me", command= button_clicked)  # Replace `None` with your function
button.pack()

#Entry
input = Entry(width = 10)
input.pack()
window.mainloop()