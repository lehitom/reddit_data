from csv import reader
rowsCount = 0
from time import sleep
import turtle
import tkinter as tk

canvasSizeX = 2000
canvasSizeY = 2000 

turtle.screensize(canvasSizeX, canvasSizeY)
myPen = turtle.Turtle()
turtle.tracer(0)
#myPen.tracer(0)
myPen.speed(1)
myPen.hideturtle() #can be reactivated
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
    #print (coordsRaw)
    coords = coordsRaw.split(",")
    xCoord = coords[0]
    yCoord = coords[1]

    myPen.forward(int(intDim) * int(xCoord))
    myPen.right(90)
    myPen.forward(int(intDim) * int(yCoord))
    myPen.setheading(0)
    box(intDim, color)

    myPen.backward(int(intDim) * int(xCoord))
    myPen.right(90)
    myPen.backward(int(intDim) * int(yCoord))
    myPen.setheading(0)
    #print ("X: " + xCoord + ", Y: " + yCoord)
    #turtle.Screen().exitonclick() 
    #quit()



boxSize = 2 #(not coord size)

#print(myPen.position())
#print(myPen.heading())

#Position myPen in top left area of the screen
myPen.penup()
#myPen.forward(-100)
#myPen.setheading(90)
#myPen.forward(100)
#myPen.setheading(0)

#print(myPen.position())
#print(myPen.heading())
myPen.backward(int(canvasSizeX)/2)
myPen.right(90)
myPen.backward(int(canvasSizeY)/2)
myPen.setheading(0)
#print(myPen.position())
#print(myPen.heading())

# Create an empty list
pixels = []
# Iterate over a sequence of numbers from 0 to 4
def storageList():
    for i in range(34): #height(Y)
        # In each iteration, add an empty list to the main list
        list_of_num = ["#FFFFFF"] * 232 #width(X)
        pixels.append(list_of_num)

#print (pixels)
#getTo(boxSize, "#0000FF", '0,0')
#getTo(boxSize, "#00FFFF", '0,0')
#getTo(boxSize, "#0000FF", '0,0')
#getTo(boxSize, "#0000FF", '0,0')

#turtle.Screen().exitonclick() 
#quit()
# open file in read mode
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
            #if(int(xCoord) <=int(232) and int(yCoord) <= int(34)):
            if (len(coords) > 2):
                print (len(coords))
            getTo(boxSize, row[2], row[3])
            #print(row[2] + ', ' + row[3])
                #print(row)
                #print (rowsCount)
            rowsCount += 1
            if rowsCount == 100000000:
                print("Terminated Early by condition")
                turtle.Screen().exitonclick() 
                quit()
            #print(row)
#print(i)

myPen.getscreen().update()	

turtle.Screen().exitonclick() 