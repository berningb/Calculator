from tkinter import *
import re


class Calculator:

    def __init__(self):

        root = Tk()

        root.resizable(width=0, height=0)
        root.title("Cool Calculator")

        entry_frame = Frame(root)
        entry_frame.grid(row=0, column=0)

        button_frame = Frame(root)
        button_frame.grid(row=4, column=0, rowspan=4)

        self.new_entry = Entry(entry_frame, width=50)
        self.new_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.create_buttons(button_frame)
        root.mainloop()

    def button_click(self, text):
        if text == '=':
            if len(self.new_entry.get()):
                try:
                    a = eval(self.new_entry.get())
                    self.new_entry.delete(0, END)
                    self.new_entry.insert(0, a)

                except ValueError:
                    print('fuck')
                    self.new_entry.delete(0, END)
                    self.new_entry.insert(0, "")
        elif text == 'clr':
            self.new_entry.delete(0, END)
        else:
            self.new_entry.insert(len(self.new_entry.get()), text)
            filtered_text = re.sub("[A-Za-z]", '', self.new_entry.get())
            self.new_entry.delete(0, END)
            self.new_entry.insert(0, filtered_text)

    def create_buttons(self, frame):
        buttons = [
            {'row': 1, 'col': 0, 'text': 7, 'color': 'white'}, {'row': 1, 'col': 1, 'text': 8, 'color': 'white'},
            {'row': 1, 'col': 2, 'text': 9, 'color': 'white'}, {'row': 1, 'col': 3, 'text': '*', 'color': '#9E9E9E'},
            {'row': 2, 'col': 0, 'text': 4, 'color': 'white'}, {'row': 2, 'col': 1, 'text': 5, 'color': 'white'},
            {'row': 2, 'col': 2, 'text': 6, 'color': 'white'}, {'row': 2, 'col': 3, 'text': '-', 'color': '#9E9E9E'},
            {'row': 3, 'col': 0, 'text': 1, 'color': 'white'}, {'row': 3, 'col': 1, 'text': 2, 'color': 'white'},
            {'row': 3, 'col': 2, 'text': 3, 'color': 'white'}, {'row': 3, 'col': 3, 'text': '+', 'color': '#9E9E9E'},
            {'row': 4, 'col': 0, 'text': 0, 'color': 'white'}, {'row': 4, 'col': 1, 'text': "clr", 'color': 'white'},
            {'row': 4, 'col': 2, 'text': "=", 'color': 'white'}, {'row': 4, 'col': 3, 'text': '/', 'color': '#9E9E9E'},
        ]

        for button in buttons:
            new_button = Button(frame, width=10, pady=20, text=button.get('text'), bg=button.get('color'), command=lambda button=button: self.button_click(button.get('text')))
            new_button.grid(row=button.get('row'), column=button.get('col'))

Calculator()
