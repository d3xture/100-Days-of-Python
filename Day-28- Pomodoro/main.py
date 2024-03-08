from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
PURPLE = "#161A30"
GRAY = "#FFFFFF"
OFF_PURPLE = "#31304D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, highlightthickness=0, bg=PURPLE)
    check_marks.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=RED, highlightthickness=0, bg=PURPLE)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=PINK, highlightthickness=0, bg=PURPLE)

    else:
        count_down(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 45, "bold"), fg=GREEN, highlightthickness=0, bg=PURPLE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_mint = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_mint:02d}:{count_sec:02d}")

    if count > 0:
        global timer
        timer = window.after(100, count_down, count - 1)
    else:
        start_timer()

        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# Screen Setup


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PURPLE)

# Canvas Setup
canvas = Canvas(width=200, height=224, bg=PURPLE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

# Label Setup
title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, highlightthickness=0, bg=PURPLE)
title_label.grid(row=0, column=1)

# Start Button
start = Button(text="Start", bg=GRAY, fg=OFF_PURPLE, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# Reset Button
reset = Button(text="Reset", bg=GRAY, fg=OFF_PURPLE, font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

# Check Mark Label
check_marks = Label(font=(FONT_NAME, 15, "bold"), bg=PURPLE, fg=GREEN, highlightthickness=0)
check_marks.grid(row=3, column=1)

window.mainloop()
