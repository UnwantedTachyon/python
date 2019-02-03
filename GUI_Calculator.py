from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg = "#5BC3F8", bd = 29,
        insertwidth = 4, width = 24,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0, "0")

        self.button1 = Button(self, bg = "#00FF00", bd = 12,
        text = "7", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonclick(7))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, bg = "#00FF00", bd = 12,
        text = "8", padx = 35, pady = 25,
        command = lambda : self.buttonclick(8), font = ("Helvetica", 20, "bold"))
        self.button2.grid(row = 2, column = 1, sticky = W)

        self.button3 = Button(self, bg = "#00FF00", bd = 12,
        text = "9", padx = 33, pady = 25,
        command = lambda : self.buttonclick(9), font = ("Helvetica", 20, "bold"))
        self.button3.grid(row = 2, column = 2, sticky = W)

        self.button4 = Button(self, bg = "#00FF00", bd = 12,
        text = "4", padx = 33, pady = 25,
        command = lambda : self.buttonclick(4), font = ("Helvetica", 20, "bold"))
        self.button4.grid(row = 3, column = 0, sticky = W)

        self.button5 = Button(self, bg = "#00FF00", bd = 12,
        text = "5", padx = 35, pady = 25,
        command = lambda : self.buttonclick(5), font = ("Helvetica", 20, "bold"))
        self.button5.grid(row = 3, column = 1, sticky = W)

        self.button6 = Button(self, bg = "#00FF00", bd = 12,
        text = "6", padx = 33, pady = 25,
        command = lambda : self.buttonclick(6), font = ("Helvetica", 20, "bold"))
        self.button6.grid(row = 3, column = 2, sticky = W)

        self.button7 = Button(self, bg = "#00FF00", bd = 12,
        text = "1", padx = 33, pady = 25,
        command = lambda : self.buttonclick(1), font = ("Helvetica", 20, "bold"))
        self.button7.grid(row = 4, column = 0, sticky = W)

        self.button8 = Button(self, bg = "#00FF00", bd = 12,
        text = "2", padx = 35, pady = 25,
        command = lambda : self.buttonclick(2), font = ("Helvetica", 20, "bold"))
        self.button8.grid(row = 4, column = 1, sticky = W)

        self.button9 = Button(self, bg = "#00FF00", bd = 12,
        text = "3", padx = 33, pady = 25,
        command = lambda : self.buttonclick(3), font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 4, column = 2, sticky = W)

        self.button9 = Button(self, bg = "#00FF00", bd = 12,
        text = "0", padx = 33, pady = 25,
        command = lambda : self.buttonclick(0), font = ("Helvetica", 20, "bold"))
        self.button9.grid(row = 5, column = 0, sticky = W)

        self.multbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "*", padx = 37, pady = 25,
        command = lambda : self.buttonclick("*"), font = ("Helvetica", 20, "bold"))
        self.multbutton.grid(row = 2, column = 3, sticky = W)

        self.addbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "+", padx = 37, pady = 25,
        command = lambda : self.buttonclick("+"), font = ("Helvetica", 20, "bold"))
        self.addbutton.grid(row = 3, column = 3, sticky = W)

        self.divbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "/", padx = 38, pady = 25,
        command = lambda : self.buttonclick("/"), font = ("Helvetica", 20, "bold"))
        self.divbutton.grid(row = 4, column = 3, sticky = W)

        self.subbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "-", padx = 36, pady = 25,
        command = lambda : self.buttonclick("-"), font = ("Helvetica", 20, "bold"))
        self.subbutton.grid(row = 5, column = 3, sticky = W)

        self.clearbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "AC", font = ("Helvetica", 20, "bold"), width = 28, padx = 7,
        command = self.ClearDisplay)
        self.clearbutton.grid(row = 1, column = 0, columnspan = 4, sticky = W)

        self.equalbutton = Button(self, bg = "#00FF00", bd = 12,
        text = "=", padx = 100, pady = 25,
        command = self.CalculateTask, font = ("Helvetica", 20, "bold"))
        self.equalbutton.grid(row = 5, columnspan = 2, column = 1, sticky = W)

    def buttonclick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invalid Syntax")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width = False, height = False)

calculator.mainloop()
