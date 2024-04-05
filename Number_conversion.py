import tkinter as tk
from tkinter import ttk
class MainApplication:
    numtoletter = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "P",
        26: "Q",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z",
    }

    lettertonum = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35,
    }

    numbercheck = {
        2: "01",
        3: "012",
        4: "0123",
        5: "01234",
        6: "012345",
        7: "0123456",
        8: "01234567",
        9: "012345678",
        10: "0123456789",
        11: "0123456789A",
        12: "0123456789AB",
        13: "0123456789ABC",
        14: "0123456789ABCD",
        15: "0123456789ABCDE",
        16: "0123456789ABCDEF",
        17: "0123456789ABCDEFG",
        18: "0123456789ABCDEFGH",
        19: "0123456789ABCDEFGHI",
        20: "0123456789ABCDEFGHIJ",
        21: "0123456789ABCDEFGHIJK",
        22: "0123456789ABCDEFGHIJKL",
        23: "0123456789ABCDEFGHIJKLM",
        24: "0123456789ABCDEFGHIJKLMN",
        25: "0123456789ABCDEFGHIJKLMNO",
        26: "0123456789ABCDEFGHIJKLMNOP",
        27: "0123456789ABCDEFGHIJKLMNOPQ",
        28: "0123456789ABCDEFGHIJKLMNOPQR",
        29: "0123456789ABCDEFGHIJKLMNOPQRS",
        30: "0123456789ABCDEFGHIJKLMNOPQRST",
        31: "0123456789ABCDEFGHIJKLMNOPQRSTU",
        32: "0123456789ABCDEFGHIJKLMNOPQRSTUV",
        33: "0123456789ABCDEFGHIJKLMNOPQRSTUVW",
        34: "0123456789ABCDEFGHIJKLMNOPQRSTUVWX",
        35: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXY",
        36: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    }

    base = ["Base-2 (Binary)", "Base-3", "Base-4", "Base-5", "Base-6", "Base-7", "Base-8 (Octal)", "Base-9", "Base-10 (Decimal)", "Base-11", "Base-12", "Base-13", "Base-14", "Base-15", "Base-16 (Hexadecimal)", "Base-17",
            "Base-18", "Base-19", "Base-20", "Base-21", "Base-22", "Base-23", "Base-24", "Base-25", "Base-26", "Base-27", "Base-28", "Base-29", "Base-30", "Base-31", "Base-32", "Base-33", "Base-34", "Base-35", "Base-36", ]

    inputnum = "" # number to be converted
    outputnum = "" # result of the conversion
    inputbase = "" # base of the inputnum
    outputbase = "" # base of the outputnum
    outputnumto = 0 # where the outputnum goes
    varx = 0 # to make it so the function "convert" doesn't run when the value of stringvar is changed not through user input
    vary = 0 # to make it so the "convert" function doesn't run infinitely at line 233

    def __init__(self, master): # setting up the window and calling functions for gui creation
        self.master = master
        self.master.title("Number system converter")
        self.master.geometry("600x200")
        self.master.resizable(True, False)

        self.label_title, self.label_equals = self.create_text()
        self.stringvar_number1, self.entry_number1, self.stringvar_number2, self.entry_number2 = self.create_number_input()
        self.combobox_base1, self.combobox_base2 = self.create_base_selection()

    def create_text(self):
        label_title = tk.Label(self.master, text="NUMBER SYSTEM CONVERTER By LOGS", font=(
            "Calibri", 18, "bold"), anchor=tk.CENTER,)
        label_title.place(x=100, y=0, width=400, height=50)

        label_equals = tk.Label(self.master, text="=", font=(
            "Calibri", 20), anchor=tk.CENTER, justify=tk.CENTER)
        label_equals.place(x=275, y=65, width=50, height=30)

        return label_title, label_equals

    def create_number_input(self): # entry(s) for input and stringvars
        stringvar_number1 = tk.StringVar()
        stringvar_number1.set("1")
        stringvar_number1.trace("w", lambda x, y, z: self.convert(2))

        entry_number1 = tk.Entry(self.master, textvariable=stringvar_number1, font=(
            "Calibri", 16), borderwidth=0, bg="lightblue",)
        entry_number1.place(x=50, y=65, width=225, height=30)

        stringvar_number2 = tk.StringVar()
        stringvar_number2.set("1")
        stringvar_number2.trace("w", lambda x, y, z: self.convert(1))

        entry_number2 = tk.Entry(self.master, textvariable=stringvar_number2, font=(
            "Calibri", 16), borderwidth=0, bg="lightgreen",)
        entry_number2.place(x=325, y=65, width=225, height=30)

        return stringvar_number1, entry_number1, stringvar_number2, entry_number2

    def create_base_selection(self): # combobox(s) for selecting the base
        combobox_base1 = ttk.Combobox(
            self.master, values=self.base, font=("Calibri", 16), state="readonly")
        combobox_base1.place(x=50, y=100, width=225, height=30)

        popdown_base1 = self.master.tk.call(
            "ttk::combobox::PopdownWindow", combobox_base1)
        self.master.tk.call(f"{popdown_base1}.f.l",
                            "configure", "-font", "Calibri 14")

        combobox_base1.current(0)

        combobox_base1.bind("<<ComboboxSelected>>",
                            lambda x: self.inputbase_or_outputbase())

        combobox_base2 = ttk.Combobox(
            self.master, values=self.base, font=("Calibri", 14), state="readonly")
        combobox_base2.place(x=325, y=100, width=225, height=30)

        popdown_base2 = self.master.tk.call(
            "ttk::combobox::PopdownWindow", combobox_base2)
        self.master.tk.call(f"{popdown_base2}.f.l",
                            "configure", "-font", "Calibri 14")

        combobox_base2.current(0)

        combobox_base2.bind("<<ComboboxSelected>>",
                            lambda x: self.inputbase_or_outputbase())

        return combobox_base1, combobox_base2

    def inputbase_or_outputbase(self): # determining if a base belongs to the input or output number
        if self.outputnumto == 2:
            self.inputbase = self.combobox_base1.get()[5:7]
            self.outputbase = self.combobox_base2.get()[5:7]
        elif self.outputnumto == 1:
            self.inputbase = self.combobox_base2.get()[5:7]
            self.outputbase = self.combobox_base1.get()[5:7]

        if self.vary == 0:
            self.convert(self.outputnumto)

    def convert(self, n): # determining which entry modified last (through stringvar tracing) + the process of converting input number in output base (outputbase determined through the previous function)
        if self.varx == 1:
            self.varx = 0
            return

        self.outputnumto = n

        if self.outputnumto == 2:
            self.inputnum = self.entry_number1.get().upper()

        elif self.outputnumto == 1:
            self.inputnum = self.entry_number2.get().upper()

        self.vary = 1
        self.inputbase_or_outputbase()
        self.vary = 0

        if not self.inputbase or not self.outputbase:
            return

        for x in self.inputnum:
            if not x in self.numbercheck[int(self.inputbase)]:
                if self.outputnumto == 1:
                    self.varx = 1
                    self.stringvar_number1.set("Invalid input")
                elif self.outputnumto == 2:
                    self.varx = 1
                    self.stringvar_number2.set("Invalid input")
                return

        base10num = self.convert_to_base10(self.inputbase, self.inputnum)
        outputnum = self.convert_to_baseo(self.outputbase, base10num)

        if self.outputnumto == 1:
            self.varx = 1
            self.stringvar_number1.set(outputnum)
        elif self.outputnumto == 2:
            self.varx = 1
            self.stringvar_number2.set(outputnum)

    def convert_to_base10(self, inputbase, inputnum): # converting inputnum to base10
        inputbase = int(inputbase)
        inputnum = inputnum[::-1]
        multiply = 1
        base10num = 0

        for x in inputnum:
            x = self.lettertonum[x]
            base10num = (x * multiply) + base10num
            multiply = multiply * inputbase

        return base10num

    def convert_to_baseo(self, outputbase, base10num): # converting inputnum to outputbase
        outputbase = int(outputbase)
        base10num = int(base10num)
        outputnum = ""

        while base10num > 0:
            outputnum = outputnum + self.numtoletter[base10num % outputbase]
            base10num = base10num // outputbase

        outputnum = outputnum[::-1]

        return outputnum


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
