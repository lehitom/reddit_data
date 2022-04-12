from tkinter import Frame, Tk
from csv import reader
rowsCount = 0


center = Tk()
#gridHeight='455'
#gridWidth='455'
cellSize=4
cellRows=34 #Y
cellCol=232 #X
gridHeight=str(cellSize*cellRows)
gridWidth=str(cellCol*cellSize)
geometryCalc = (gridWidth+"x"+gridHeight) 
center.geometry(geometryCalc)
center.title("R/Place")

colorCell = '#FF0000'

cells = {}
for row in range(cellRows):
     for column in range(cellCol):
        cell = Frame(center, bg='white', 
                     width=cellSize, height=cellSize)
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell

def color_cell(cells, i, j):
    cells[(i, j)].configure(background=colorCell)

def sampleTest():
    print("before")
    #center.after(0, color_cell, cells, 3, 4)
    center.after(0, color_cell, cells, 0, 0)
    center.after(0, color_cell, cells, 0, 1)
    center.after(0, color_cell, cells, 1, 1)
    center.after(0, color_cell, cells, 2, 2)
    center.update()
    center.after(0, color_cell, cells, 3, 3)
    center.after(0, color_cell, cells, 4, 4)
    center.after(0, color_cell, cells, 5, 5)
    center.after(0, color_cell, cells, 6, 6)
    center.after(0, color_cell, cells, 7, 7)
    center.after(0, color_cell, cells, 8, 8)
    center.after(0, color_cell, cells, 8, 7)
    print("after")


#sampleTest()




center.update()
center.mainloop()