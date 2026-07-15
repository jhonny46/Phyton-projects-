from pickle import GLOBAL
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_lb.config(text ="Timer")
    canvas.itemconfig(timer_text , text="00:00")
    check_mark.config(text ="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shor_break_sec =  SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        # Count down for long break rep 8
        count_down(long_break_sec)
        timer_lb.config(text="BREAK", fg= RED)
    elif reps % 2 == 0:
        # Count down for the first rep 2,4,6
        count_down(shor_break_sec)
        timer_lb.config(text="BREAK", fg=PINK)
    else:
        # Count down for the first rep 1,3,5,7
        count_down(work_sec)
        timer_lb.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global  reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    print(reps)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")# To change a canvas element you use itemconfig()
    if count > 0:
        global timer
        timer = window.after(1, count_down, count-1) # counts down -1 evey second
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark +="✅"
        check_mark.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg = YELLOW)



canvas = Canvas(width=200, height =224, bg = YELLOW, highlightthickness=0  )
tomato_image= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image = tomato_image)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))

canvas.grid(column = 1, row = 1)


# Lables

timer_lb = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg= GREEN)
timer_lb.grid(column = 1, row = 0)

check_mark = Label(font=(FONT_NAME, 35),bg=YELLOW, fg= GREEN)
check_mark.grid(column = 1, row = 3)

#Buttons
start_button = Button(text="Start", highlightthickness= 0, command = start_timer)
start_button.grid(column= 0, row= 2)

reset_button = Button(text="Reset",font=(FONT_NAME), highlightthickness = 0, command= reset_timer)
reset_button.grid(column= 2, row = 2)
window.mainloop()