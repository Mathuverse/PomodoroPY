import math
from tkinter import *

#Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = None


#Timer Reset
timer_is_on = True

#Reset the timer
def reset_timer():
    global reps,timer
    start.config(state="active")
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=RED)
    check_label.config(text="")
    

#Timer Mechanism
#Countdown mechanism

#Add checkmarks when work session completed 
def add_check():
    global checkmarks
    checkmarks = f"{checkmarks}✓"
    check_label.config(text=checkmarks)

#Clear all the checkmarks
def clear_check():
    global checkmarks
    checkmarks = ""
    check_label.config(text=checkmarks)

#Mechanism for countdown
def count_down(count):
    if timer_is_on:
        count_min = math.floor(count/60)
        count_sec = count% 60
        if count_sec < 10 and count_sec > -1:
            canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
        else:
            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            global timer
            timer = window.after(1000,count_down,count - 1)
        else:
            start_timer()

#Make the start mechanism for the 25, 5 , 20 mins timer
def start_timer():
    global reps,clickStart,clickReset
    start.config(state="disabled")
    reps+=1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_Sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%2 == 1:
        timer_label.config(text="Work",fg=YELLOW)
        count_down(work_sec)

    elif reps % 8 == 0:
        timer_label.config(text="Long Break",fg=PINK)
        count_down(long_break_sec)
        clear_check()

    elif reps % 2 == 0:
        add_check()
        timer_label.config(text="Short Break")
        count_down(short_break_Sec)

#Window settings
window = Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20,bg= GREEN)


#Image
canvas = Canvas(width=200,height=224,bg= GREEN, highlightthickness= 0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
timer_text = canvas.create_text(100,125,text="00:00",font=(FONT_NAME,35,"bold"))
canvas.grid(row =1,column=1)

#label
timer_label = Label(text="Timer",bg=GREEN,fg=RED,font=("Arial",30,"bold"))
timer_label.grid(row= 0,column=1)
check_label = Label(text=checkmarks,bg=GREEN,fg=RED,font=("Arial",15,"bold"))
check_label.grid(row=4,column=1)

#Button

start = Button(text="Start",bg=GREEN,highlightthickness=0,highlightbackground=GREEN,fg=RED,command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="Reset",bg=GREEN,highlightthickness=0,highlightbackground=GREEN,fg=RED,command=reset_timer)
reset.grid(row=2,column=2)







window.mainloop()