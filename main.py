import math
from tkinter import *

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
window_function = None


# ---------------------------- TIMER RESET  ------------------------------- #
def reset_timer():
    window.after_cancel(f"{window_function}")
    canvas.itemconfig(timer_canvas, text="00:00")
    timer_text.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    #   if reps is in the 8th

    if reps % 8 == 0:
        countdown(1200)
        timer_text.config(text="Time For Long Break!")

    # if reps is in the 2nd/4th and 6th

    elif reps % 2 == 0:
        countdown(300)
        timer_text.config(text="Time For Short Break!")


    #     if reps is in the 1st/3rd/5th and 7th

    else:
        countdown(1500)
        timer_text.config(text="Time For Work!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    if count >= 0:
        global window_function
        canvas.itemconfig(timer_canvas, text=f"{count_min}:{count_sec}")
        window_function = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_section = count / 2
        for _ in range(math.floor(work_section)):
            mark += "✔"

            checkmark.config(text=f"{mark}")


# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Pomadoras")
window.config(padx=100, pady=50, bg=GREEN)

# photo image
photo_image = PhotoImage(file="tomato.png")

# canvas
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
canvas.create_image(100, 112, image=photo_image)
timer_canvas = canvas.create_text(100, 130, text="0", fill="white", font=("Aries", 13, "bold"))
canvas.grid(column=2, row=2)

countdown(1500)

# label
timer_text = Label(text="Timer", font=("aries", 15, "bold"), fg=PINK, bg=GREEN)
timer_text.grid(column=2, row=0)
checkmark = Label(text="", font=("aries", 15, "bold"), fg=PINK, bg=GREEN)
checkmark.grid(column=2, row=4)

# button
start = Button(text="Start", font=("aries", 13, "bold"), highlightthickness=0, fg=GREEN, bg=PINK, command=start_timer)
start.grid(column=0, row=4)
reset = Button(text="Reset", font=("aries", 13, "bold"), highlightthickness=0, fg=GREEN, bg=PINK, command=reset_timer)
reset.grid(column=4, row=4)

# window mainloop
window.mainloop()
