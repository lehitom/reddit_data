from csv import reader
rowsCount = 0
from time import sleep
import turtle
import tkinter as tk

canvasSizeX = 9000
canvasSizeY = 11000 

root = tk.Tk()

canvas = turtle.ScrolledCanvas(root)
canvas.pack(side=tk.LEFT)


screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(0, canvasSizeY, canvasSizeX, 0)

turtle = turtle.RawTurtle(screen)
turtle.goto(9000, 11000)

#screen.mainloop()
#RawTurtle.Screen().exitonclick() 
#quit()



#myPen = turtle.Turtle()
myPen = turtle
#turtle.tracer(0)
#turtle.screensize(canvasSizeX, canvasSizeY)
#myPen.tracer(0)
myPen.speed(1)
#myPen.hideturtle() #can be reactivated
#myPen.color("#000000")

colourPalette = [
"#FFFFFF","#E4E4E4","#888888","#222222",
"#FFA7D1","#E50000","#E59500","#A06A42",
"#E5D900","#94E044","#02BE01","#00E5F0",
"#0083C7","#0000EA","#E04AFF","#820080"]

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim, color):
    #sleep(1)
    myPen.color(color)
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.right(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.right(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.right(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
    myPen.getscreen().update()
    



def getTo(intDim, color, coordsRaw):
    print (coordsRaw)
    coords = coordsRaw.split(",")
    xCoord = coords[0]
    yCoord = coords[1]

    myPen.forward(int(intDim) * int(xCoord))
    myPen.right(90)
    myPen.forward(int(intDim) * int(yCoord))
    myPen.setheading(0)
    box(intDim, color)
    #print ("X: " + xCoord + ", Y: " + yCoord)
    #quit()



boxSize = 10 #(not coord size)

#print(myPen.position())
#print(myPen.heading())

#Position myPen in top left area of the screen
myPen.penup()
#myPen.forward(-100)
#myPen.setheading(90)
#myPen.forward(100)
#myPen.setheading(0)

print(myPen.position())
print(myPen.heading())
#myPen.setheading(180)
#myPen.forward(int(boxSize) * int(canvasSizeX/2))
#myPen.setheading(270)
#myPen.forward(int(boxSize) * int(canvasSizeY/2))
#myPen.setheading(0)

# Create an empty list
pixels = []
# Iterate over a sequence of numbers from 0 to 4
for i in range(1100): #height
    # In each iteration, add an empty list to the main list
    list_of_num = ["#FFFFFF"] * 900 #depth
    pixels.append(list_of_num)

#print (pixels)
getTo(boxSize, "#0000FF", '0,0')


#quit()
# open file in read mode
with open('2022_place_canvas_history.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        next(csv_reader, None) #skips the headers
        # Iterate over each row in the Csv using reader objust
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            getTo(boxSize, row[2], row[3])
            #print(row[2] + ', ' + row[3])
            print(row)
            rowsCount += 1
            if rowsCount == 1:
                turtle.Screen().exitonclick() 
                quit()
            #print(row)
#print(i)

myPen.getscreen().update()	

turtle.Screen().exitonclick() 