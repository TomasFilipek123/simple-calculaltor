"""Simple Calculator App"""

import tkinter as tk
from tkinter import ttk
width = 400
height = 343


class CalcFrame(ttk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.options = {'ipadx': 5, 'ipady': 10}
        self.style = ttk.Style()
        self.columnconfigure([0, 1, 2, 3], weight=1)
        self.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
        # Configure properties of the buttons
        self.style.theme_use('default')
        self.style.configure('small.TButton', font=(None, 15), foreground='black')
        self.style.configure('big.TButton', font=(None, 15), foreground='black', background='yellow')
        self.__create_widgets()

    def __create_widgets(self):
        # Configure properties of the buttons
        # self.style.configure('small.TButton', font=(None, 15), foreground='blue4')

        # Entry
        entry_variable = tk.StringVar()
        self.entry = ttk.Entry(self, font=('Calibri', 30), textvariable=entry_variable, justify='right')
        self.entry.grid(column=0, row=0, columnspan=4, ipadx=5, ipady=10)
        # buttons
        # clear button
        c_button = ttk.Button(self,
                              text='C',
                              command=lambda: self.entry.delete(len(self.entry.get())-1, tk.END),
                              style='small.TButton')
        c_button.grid(column=0, row=1, columnspan=2, sticky='we', **self.options)
        # '%' button
        percent_button = ttk.Button(self,
                                    text='%',
                                    style='small.TButton',
                                    command=lambda: self.entry.insert(tk.END, '%'))
        percent_button.grid(column=2, row=1, sticky='w', **self.options)
        # operation buttons
        divide = ttk.Button(self,
                            text='÷',
                            style='big.TButton',
                            command=lambda: self.entry.insert(tk.END, '÷'))
        divide.grid(row=1, column=3, sticky='w', **self.options)
        multiply = ttk.Button(self,
                              text='×',
                              style='big.TButton',
                              command=lambda: self.entry.insert(tk.END, '×'))
        multiply.grid(row=2, column=3, sticky='w', **self.options)
        subtract = ttk.Button(self,
                              text='-',
                              style='big.TButton',
                              command=lambda: self.entry.insert(tk.END, '-'))
        subtract.grid(row=3, column=3, sticky='w', **self.options)
        add = ttk.Button(self,
                         text='+',
                         style='big.TButton',
                         command=lambda: self.entry.insert(tk.END, '+'))
        add.grid(row=4, column=3, sticky='w', **self.options)

        # self.divide_button = ttk.Button(self, text=':', style='small.TButton')
        # self.divide_button.grid(column=3, row=1, sticky='w', **self.options)
        # numbers
        zero = ttk.Button(self,
                          text=str(0),
                          style='small.TButton',
                          command=lambda: self.entry.insert(tk.END, '0'))
        zero.grid(row=5, columnspan=2, sticky='we', **self.options)

        one = ttk.Button(self,
                         text=str(1),
                         style='small.TButton',
                         command=lambda: self.entry.insert(tk.END, '1'))
        one.grid(row=4, column=0, sticky='w', **self.options)

        two = ttk.Button(self,
                         text=str(2),
                         style='small.TButton',
                         command=lambda: self.entry.insert(tk.END, '2'))
        two.grid(row=4, column=1, sticky='w', **self.options)

        three = ttk.Button(self,
                           text=str(3),
                           style='small.TButton',
                           command=lambda: self.entry.insert(tk.END, '3'))
        three.grid(row=4, column=2, sticky='w', **self.options)

        four = ttk.Button(self,
                          text=str(4),
                          style='small.TButton',
                          command=lambda: self.entry.insert(tk.END, '4'))
        four.grid(row=3, column=0, sticky='w', **self.options)

        five = ttk.Button(self,
                          text=str(5),
                          style='small.TButton',
                          command=lambda: self.entry.insert(tk.END, '5'))
        five.grid(row=3, column=1, sticky='w', **self.options)

        six = ttk.Button(self,
                         text=str(6),
                         style='small.TButton',
                         command=lambda: self.entry.insert(tk.END, '6'))
        six.grid(row=3, column=2, sticky='w', **self.options)

        seven = ttk.Button(self,
                           text=str(7),
                           style='small.TButton',
                           command=lambda: self.entry.insert(tk.END, '7'))
        seven.grid(row=2, column=0, sticky='w', **self.options)

        eight = ttk.Button(self,
                           text=str(8),
                           style='small.TButton',
                           command=lambda: self.entry.insert(tk.END, '8'))
        eight.grid(row=2, column=1, sticky='w', **self.options)

        nine = ttk.Button(self,
                          text=str(9),
                          style='small.TButton',
                          command=lambda: self.entry.insert(tk.END, '9'))
        nine.grid(row=2, column=2, sticky='w', **self.options)

        # point button
        point = ttk.Button(self,
                           text='.',
                           style='small.TButton',
                           command=lambda: self.entry.insert(tk.END, '.'))
        point.grid(row=5, column=2, sticky='w', **self.options)

        # equal button
        equal = ttk.Button(self,
                           text='=',
                           style='big.TButton',
                           command=self.result)
        equal.grid(row=5, column=3, sticky='w', **self.options)

        # Add padding to the frame and show it
        self.pack()

    def result(self):
        result = list(self.entry.get())
        for i in range(len(result)):
            if result[i] == '×':
                result[i] = '*'
            elif result[i] == '÷':
                result[i] = '/'
            elif result[i] == '%':
                result[i] = '*0.01*'
        self.entry.delete(0, 'end')
        self.entry.insert(0, eval(''.join(result)))


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simple Calculator')
        self.geometry(f'{width}x{height}')
        self.resizable(False, False)


if __name__ == '__main__':
    app = App()
    CalcFrame(app)
    app.mainloop()
