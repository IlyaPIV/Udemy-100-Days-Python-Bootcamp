from tkinter import *


def convert_miles_to_km():
    miles = miles_input.get()
    km = 1.609 * float(miles)
    km_result_label.config(text=f"{round(km, 2)}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_km)
calculate_button.grid(row=2, column=1)


window.mainloop()
