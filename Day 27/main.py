import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(500, 300)

#To print lables in Tkinter you need to  create the lable objct and use pack()
my_label = tkinter.Label( text ="I am label", font = ("Arial", 24, "bold"))
#my_label.pack()
# my_label.pack(side = "left")
# my_label.pack(side = "right")
# my_label.pack(side = "top")
# my_label.pack(side = "bottom")
# my_label.pack(expand = True)


window.mainloop()

# import turtle
#
# screen = turtle.Screen()
# screen
# screen.exitonclick()
