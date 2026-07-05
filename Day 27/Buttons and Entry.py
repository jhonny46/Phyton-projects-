from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx = 100, pady = 200)

# Label
my_lable = Label(text = "I am a Label", font=("Arial", 24, "bold"))
my_lable.grid(column = 0, row = 0)

#my_lable.place(x = 50, y= 100)

my_lable["text"] = "NewText"
my_lable.config(text = "New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_lable.config(text=new_text)

button = Button(text="Click Me", command= button_clicked)  # Replace `None` with your function
button.grid(column = 3, row = 1)

new_button = Button(text = "New_Button")
new_button.grid(column = 4, row =0)
#Entry
input = Entry(width = 10)
input.grid(column = 5, row = 4)
window.mainloop()