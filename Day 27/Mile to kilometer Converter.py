from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height = 200)
window.config(padx = 100, pady= 50)

def mk_to_km():
    miles = entry_1.get()
    km = float(miles) * 1.609
    text_4.config(text= km)

# Lable

text_1 = Label(text = "is equal to", font=("Arial", 24))

text_1.grid(column = 0, row =1)
text_1.config(padx = 5, pady= 10)

text_2 = Label(text = "miles", font=("Arial", 24))
text_2.grid(column = 2, row =0)
text_2.config(padx = 5, pady= 10)

text_3 = Label(text = "KM", font=("Arial", 24))
text_3.grid(column = 2, row =1)
text_3.config(padx = 5, pady= 10)


text_4 = Label(text = "0", font=("Arial", 24))
text_4.grid(column = 1, row =1)
text_4.config(padx = 5, pady= 10)

# Entry
entry_1 = Entry(width= 10)
entry_1.grid(column = 1, row =0)

# Buttons
button = Button(text = "Calculate", command= mk_to_km)
button.grid(column = 1, row =2)
button.config(padx = 2, pady= 1)


window.mainloop()