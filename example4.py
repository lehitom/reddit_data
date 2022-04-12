from tkinter import Frame, Tk


center = Tk()
gridHeight='455'
gridWidth='455'
geometryCalc = (gridWidth+"x"+gridHeight) 
center.geometry(geometryCalc)
#center.geometry('455x455')
center.title("9x9 grid")

colorCell = '#FF0000'

cells = {}
for row in range(9):
     for column in range(9):
        cell = Frame(center, bg='white', 
                     width=50, height=50, padx=3, pady=3)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell


def color_cell(cells, i, j):
    cells[(i, j)].configure(background=colorCell)
def color_cell2(cells, i, j):
    cells[(i, j)].configure(background='#00FF00')

print("before")
#center.after(0, color_cell, cells, 3, 4)
center.after(0, color_cell, cells, 0, 0)
center.after(0, color_cell, cells, 0, 1)
center.after(0, color_cell, cells, 1, 1)
center.after(0, color_cell, cells, 2, 2)
center.after(0, color_cell, cells, 3, 3)
center.after(0, color_cell, cells, 4, 4)
center.after(0, color_cell, cells, 5, 5)
center.after(0, color_cell, cells, 6, 6)
center.after(0, color_cell, cells, 7, 7)
center.after(0, color_cell, cells, 8, 8)
#center.after(0, color_cell, cells, 9, 9)
print("after")
center.mainloop()