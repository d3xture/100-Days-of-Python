from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def converter():
    value = float(input_entry.get())
    answer = round(value * 1.609)
    output = Label()
    output["text"] = answer
    output.grid(column=1, row=1)


# Labels

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)


# Entry
input_entry = Entry(width=10)
print(input_entry.get())
input_entry.grid(column=1, row=0)


# Button
button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)


window.mainloop()
