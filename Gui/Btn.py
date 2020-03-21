from _ast import Lambda
from tkinter import *


class Btn:
    def __init__(self, frame, row, column, text, color):
        self._frame = frame
        self._row = row
        self._column = column
        self._text = text
        self._color = color


    def click_button(self):
        print(self._text)

