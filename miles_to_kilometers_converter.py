from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 500, height= 300)
window.config(padx = 30, pady = 30)

def mile_to_kilometer():
    mile = float(miles_input.get())
    km = round(mile * 1.609)
    kilometer_result_label.config(text = f"{km}")

miles_input = Entry(width = 7,)
miles_input.grid(column = 1, row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

is_equal_to_label = Label(text = "Is equal to")
is_equal_to_label.grid(column = 0, row = 1)

kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(column = 1, row = 1)

kilometer_label = Label(text = "Km")
kilometer_label.grid(column = 2, row = 1)

calculate_button = Button(text = "Calculate", command=mile_to_kilometer)
calculate_button.grid(column = 1, row = 2)








window.mainloop()