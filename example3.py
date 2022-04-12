from tkinter import Frame, Tk


center = Tk()
center.geometry('455x455')
center.title("9x9 grid")

cells = {}
for row in range(9):
     for column in range(9):
        cell = Frame(center, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=50, height=50, padx=3, pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell


def color_cell(cells, i, j, color="red"):
    cells[(i, j)].configure(background="red")


center.after(5000, color_cell, cells, 3, 4)

center.mainloop()