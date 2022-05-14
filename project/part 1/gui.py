import csv
from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        self.frame_function = Frame(self.window)
        self.label_function = Label(self.frame_function, text='Function')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_sum = Radiobutton(self.frame_function, text='Sum', variable=self.radio_1, value=1)
        self.radio_power = Radiobutton(self.frame_function, text='Power', variable=self.radio_1, value=2)
        self.label_function.pack(side='left')
        self.radio_sum.pack(side='left')
        self.radio_power.pack(side='left')
        self.frame_function.pack(anchor='w')

        self.frame_start = Frame(self.window)
        self.label_start = Label(self.frame_start, text='Start')
        self.entry_start = Entry(self.frame_start)
        self.label_start.pack(padx=30, side='left')
        self.entry_start.pack(padx=30, side='left')
        self.frame_start.pack(anchor='w', pady=5)
        self.frame_stop = Frame(self.window)
        self.label_stop = Label(self.frame_stop, text='Stop')
        self.entry_stop = Entry(self.frame_stop)
        self.label_stop.pack(padx=30, side='left')
        self.entry_stop.pack(padx=30, side='left')
        self.frame_stop.pack(anchor='w', pady=5)

        self.frame_base = Frame(self.window)
        self.label_base = Label(self.frame_base, text='Base')
        self.entry_base = Entry(self.frame_base)
        self.label_base.pack(padx=30, side='left')
        self.entry_base.pack(padx=30, side='left')
        self.frame_base.pack(anchor='w', pady=5)
        self.frame_exponent = Frame(self.window)
        self.label_exponent = Label(self.frame_exponent, text='Exponent')
        self.entry_exponent = Entry(self.frame_exponent)
        self.label_exponent.pack(padx=30, side='left')
        self.entry_exponent.pack(padx=30, side='left')
        self.frame_exponent.pack(anchor='w', pady=5)

        self.frame_bottom = Frame(self.window)
        self.button_submit = Button(self.frame_bottom, text='Submit', command=self.clicked)
        self.button_submit.pack()
        self.frame_bottom.pack()

        self.frame_bottom = Frame(self.window)
        self.button_clear = Button(self.frame_bottom, text='Clear', command=self.clicked)
        self.button_clear.pack()
        self.frame_bottom.pack()

    def forget(self):
        self.forget()

    def clicked(self):

        start = self.entry_start.get()
        stop = self.entry_stop.get()
        base = self.entry_base.get()
        exponent = self.entry_exponent.get()
        function = self.radio_1.get()

        if function == 1:
            function = 'Sum'

        elif function == 2:
            function = 'Power'

        with open('records.csv', 'a', newline='') as file:
            content = csv.writer(file)
            content.writerow([stop, start, function])([base, exponent, function])

        self.entry_start.delete(0, END)
        self.entry_stop.delete(0, END)
        self.entry_base.delete(0, END)
        self.entry_exponent.delete(0, END)
        self.radio_1.set(0)
