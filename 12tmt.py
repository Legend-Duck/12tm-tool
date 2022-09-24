import tkinter as tk
import random as rn

class Main(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        root.title('12-tone Matrix')
        root.rowconfigure(index=0, weight=1)
        root.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=[0, 1], weight=1)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.grid_frame = Grid(self)
        self.command = Command(self.grid_frame)
        self.button_frame = Button(self, self.command)

class Button(tk.Frame):
    def __init__(self, main, command):
        super().__init__(main)
        self.grid(row=0, column=1, sticky=tk.NW)
        self.type = {'Auto-fill': 'auto_fill', 'Random': 'random', 'Clear': 'clear'}
        self.key = list(self.type.keys())
        for key in self.key:
            tk.Button(self, text=key, command=getattr(command, self.type[key])).grid(row=self.key.index(key), column=0, sticky=tk.EW)

class Grid(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.rowconfigure(index=list(range(12)), weight=1)
        self.columnconfigure(index=list(range(12)), weight=1)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.entry = []
        for row in range(12):
            tmp = [tk.Entry(self, justify=tk.CENTER, width=3, font=('Arial',10)) for _ in range(12)]
            self.entry.append(tmp)
            for column in range(12):
                tmp[column].grid(row=row, column=column, sticky=tk.NSEW)

class Command:
    def __init__(self, grid_frame):
        self.grid_frame = grid_frame
        self.num = list(range(12))

    def auto_fill(self):
        dia = self.grid_frame.entry[0][0].get()
        if not(dia.isdigit()): return
        for row in range(1, 12):
            self.grid_frame.entry[row][row].delete('0', 'end')
            self.grid_frame.entry[row][row].insert('0', dia)
        for row in range(1, 12):
            r0 = self.grid_frame.entry[0][row].get()
            if not(r0.isdigit()): continue
            diff = int(dia) - int(r0)
            for column in range(12):
                r0 = self.grid_frame.entry[0][column].get()
                if not(r0.isdigit()): continue
                self.grid_frame.entry[row][column].delete('0', 'end')
                self.grid_frame.entry[row][column].insert('0', (int(r0) + diff + 12) % 12)

    def random(self):
        rn.shuffle(self.num)
        for i in range(12):
            self.grid_frame.entry[0][i].delete('0', 'end')
            self.grid_frame.entry[0][i].insert('0', self.num[i])
        self.auto_fill()

    def clear(self):
        for row in range(12):
            for column in range(12):
                self.grid_frame.entry[row][column].delete('0', 'end')

def main():
    root = tk.Tk()
    app = Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()