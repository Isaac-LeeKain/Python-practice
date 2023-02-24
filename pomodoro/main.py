import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
TOMATO_PNG_PATH = r'D:\\Project\\VisualStudioCode\\Python\\pomodoro-start\\tomato.png'
LABEL_1_TEXT = ['Timer', 'Work', 'Break', 'Pause']
LABEL_2_TEXT = ['', '✔', '✔✔', '✔✔✔', '✔✔✔✔']


# ---------------------------- TIMER RESET ------------------------------- #
# Reset_click
def button_2_click():
    toggle.set(False)
    reps.set(1)
    timer.set(WORK_MIN * 60)
    count_min = str(math.floor(timer.get() / 60)).rjust(2, '0')
    count_sec = str(timer.get() % 60).rjust(2, '0')
    canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
    button_1_start.config(text='Start')
    # Reset => label(timer,green) / label(no_checkmark)
    label_1_title.config(text=LABEL_1_TEXT[0], fg=GREEN)
    label_2_check.config(text=LABEL_2_TEXT[math.floor(reps.get() / 2)])


# ---------------------------- TIMER MECHANISM ------------------------------- #
# start_click
def button_1_click():
    toggle.set(not toggle.get())
    if toggle.get():
        if reps.get() % 8 == 0:
            # Long_break => label(break,red)
            label_1_title.config(text=LABEL_1_TEXT[2], fg=RED)
        elif reps.get() % 2 == 0:
            # Short_break => label(break,pink)
            label_1_title.config(text=LABEL_1_TEXT[2], fg=PINK)
        else:
            # Work => label(work,green)
            label_1_title.config(text=LABEL_1_TEXT[1], fg=GREEN)
        label_2_check.config(text=LABEL_2_TEXT[math.floor(reps.get() / 2)])
        button_1_start.config(text='Pause')
        time_cal()
    else:
        # Pause => button(Start) / label(Pause,black)
        button_1_start.config(text='Start')
        label_1_title.config(text=LABEL_1_TEXT[3], fg='black')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def time_cal():
    if toggle.get():

        count_min = str(math.floor(timer.get() / 60)).rjust(2, '0')
        count_sec = str(timer.get() % 60).rjust(2, '0')
        canvas.itemconfig(canvas_text, text=f'{count_min}:{count_sec}')
        # Time calculation
        if timer.get() > 0:
            timer.set(timer.get() - 1)
            _callback_id.set(root.after(100, time_cal))
        # Set new time
        else:
            reps.set(reps.get() + 1)
            if reps.get() % 8 == 0:
                timer.set(LONG_BREAK_MIN * 60)
                reps.set(0)
            elif reps.get() % 2 == 0:
                timer.set(SHORT_BREAK_MIN * 60)
            else:
                timer.set(WORK_MIN * 60)
            toggle.set(not toggle.get())
            # Start again
            button_1_click()
    else:
        # record function
        root.after_cancel(_callback_id.get())


# ---------------------------- UI SETUP ------------------------------- #
# Window
root = tk.Tk()
root.title('Pomodoro')
root.config(padx=100, pady=50, bg=YELLOW)
# Rep
reps = tk.IntVar(root)
reps.set(1)
# Timer
timer = tk.IntVar(root)
timer.set(WORK_MIN * 60)
# Toggle
toggle = tk.BooleanVar(root)
toggle.set(False)
# Callback
_callback_id = tk.StringVar(root)
_callback_id.set(None)
# Canvas
tomato_img = tk.PhotoImage(file=TOMATO_PNG_PATH)
canvas = tk.Canvas(width=250, height=300)
canvas.create_image(125, 160, image=tomato_img)
canvas.config(bg=YELLOW, highlightthickness=0)
canvas_text = canvas.create_text(125,
                                 180,
                                 text='25:00',
                                 fill="white",
                                 font=(FONT_NAME, 32, 'bold'))
canvas.grid(column=1, row=1)

# Label
label_1_title = tk.Label(text=LABEL_1_TEXT[0],
                         font=(FONT_NAME, 36, 'bold'),
                         bg=YELLOW,
                         fg=GREEN)
label_1_title.grid(column=1, row=0)

label_2_check = tk.Label(text=LABEL_2_TEXT[0],
                         font=(FONT_NAME, 12, 'bold'),
                         bg=YELLOW,
                         fg=GREEN)
label_2_check.config(pady=10)
label_2_check.grid(column=1, row=3)

# Button
button_1_start = tk.Button(text='Start',
                           command=button_1_click,
                           font=(FONT_NAME, 16, 'bold'),
                           bg='white',
                           highlightthickness=0)
button_1_start.grid(column=0, row=2)

button_2_reset = tk.Button(text='Reset',
                           command=button_2_click,
                           font=(FONT_NAME, 16, 'bold'),
                           bg='white',
                           highlightthickness=0)
button_2_reset.grid(column=2, row=2)

# Loop
root.mainloop()
