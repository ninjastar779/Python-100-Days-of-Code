import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.result = ''
        self.create_widgets()

    def create_widgets(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'D'
        ]
        row_val = 0
        col_val = 0
        for button in buttons:
            tk.Button(self.master, text=button, width=5,
                      command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.result_label = tk.Label(self.master, text=self.result, width=20)
        self.result_label.grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.result)
                self.result = str(result)
            except Exception as e:
                self.result = 'Error'
        elif button == 'C':
            self.result = ''
        elif button == 'D':
            self.result = self.result[:-1]
        else:
            self.result += button

        self.result_label['text'] = self.result

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()

