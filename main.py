from tkinter import *
import time

# Constants
BG_COLOR = "#1E1D22"
current_text = ""
secondes = 2

# ---------- SET TKINTER ---------- #
app = Tk()
app.title("Text Disapearing Desktop App")
app.minsize(width=800, height=800)
app.maxsize(width=800, height=800)
app.config(bg=BG_COLOR, padx=30, pady=30)


# --------------------------------- #


# Function to disappear text
def count():
    global current_text
    global new_text
    global secondes
    if secondes <= 0:
        text_to_kill.delete("1.0", "end")
        quote_lab.config(text="☠  Text Killed  ☠", font=("Arial", 26, "bold"))
        text_to_kill.config(width=55, height=15, font=("Arial", 14, "normal"))
        secondes = 2
        print("delete")
        print(secondes)
    else:
        app.update()
        secondes -= 1
        print(secondes)
        quote_lab.config(text=f"{secondes}", font=("Arial", 22, "bold"))
        text_to_kill.config(fg="red")
        text_to_kill.config(width=55, height=15, font=("Arial", 14, "normal"))
        time.sleep(0.1)
        app.update()
        text_to_kill.config(fg="red")
        text_to_kill.config(width=55, height=15, font=("Arial", 14, "normal"))
        time.sleep(0.1)
        app.update()
        app.after(1000, count)


def text_killer():
    global current_text
    global new_text
    quote_lab.config(text="", font=("Arial", 18, "normal"))
    new_text = text_to_kill.get("1.0", "end")
    if new_text == current_text and len(current_text) - 1 != 0:
        count()
        print("RIP text !")
    text_to_kill.config(fg=BG_COLOR)
    current_text = new_text
    app.after(6000, text_killer)


# ---------- GUI ---------- #

# Title :
title_lab = Label(app, text="Text Disappearing App", width=20, font=("Calibri", 30, "bold"))
title_lab.config(fg="gray90", bg=BG_COLOR, anchor="center")
title_lab.pack(padx=30, pady=15, anchor="center")

# red :
red = Label(app, text="o ° o", width=40, font=("Arial", 18, "bold"))
red.config(fg="#ff4d4d", bg=BG_COLOR, anchor="center")
red.pack(padx=30, pady=15, anchor="center")

# Subtitle :
subtitle_lab = Label(app, text="Text is gonna disappear after 10s of inactivity", width=50, font=("Arial", 10))
subtitle_lab.config(fg="gray40", bg=BG_COLOR, anchor="center")
subtitle_lab.pack(padx=30, pady=15, anchor="center")

# Text to kill :
text_to_kill = Text(app, width=55, height=15, font=("Arial", 14, "normal"))
text_to_kill.config(fg=BG_COLOR, bg="gray90", bd=30, relief="flat", insertwidth=5, insertbackground="red", cursor="")
text_to_kill.focus()
text_to_kill.pack()

# red :
red2 = Label(app, text="° o °", width=40, font=("Arial", 18, "bold"))
red2.config(fg="#ff4d4d", bg=BG_COLOR, anchor="center")
red2.pack(padx=30, pady=30, anchor="center")

# quote :
quote_lab = Label(app, text="This text is so dead", width=40, font=("Arial", 18, "bold"))
quote_lab.config(fg="#ff4d4d", bg=BG_COLOR, anchor="center")
quote_lab.pack(padx=30, pady=0, anchor="center")

app.after(6000, text_killer)
app.mainloop()
