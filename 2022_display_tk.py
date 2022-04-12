from tkinter import Frame, Tk
from csv import reader
rowsCount = 0


center = Tk()
#gridHeight='455'
#gridWidth='455'
cellSize=6
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

newColor = "FFFFFF"

def color_cell(cells, i, j):
    cells[(i, j)].configure(background=newColor)

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

with open('2022_place_canvas_history.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        next(csv_reader, None) #skips the headers
        # Iterate over each row in the Csv using reader objust
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            coords = row[3].split(",")
            xCoord = coords[0]
            yCoord = coords[1]
            if(int(xCoord) <=int(232) and int(yCoord) <= int(34)):
                print (len(coords))
                newColor = row[2]
                center.after(0, color_cell, cells, int(yCoord), int(xCoord))
                center.update()
            #getTo(boxSize, row[2], row[3])
            #print(row[2] + ', ' + row[3])
                #print(row)
                #print (rowsCount)
            rowsCount += 1
            if rowsCount == 1000000:
                print("Terminated Early by condition")
                center.mainloop()
                #turtle.Screen().exitonclick() 
                quit()




center.update()
center.mainloop()