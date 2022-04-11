from time import sleep
import turtle

myPen = turtle.Turtle()
turtle.tracer(0)
#myPen.tracer(0)
myPen.speed(1)
myPen.hideturtle()
#myPen.color("#000000")


colourPalette = [
"#FFFFFF","#E4E4E4","#888888","#222222",
"#FFA7D1","#E50000","#E59500","#A06A42",
"#E5D900","#94E044","#02BE01","#00E5F0",
"#0083C7","#0000EA","#E04AFF","#820080"]

# Create an empty list
pixels = []
# Iterate over a sequence of numbers from 0 to 4
for i in range(10):
    # In each iteration, add an empty list to the main list
    list_of_num = [0] * 10
    pixels.append(list_of_num)
#print('List of lists:')
#print(pixels)

pixels[0][0]=0
pixels[1][1]=1
pixels[2][2]=2
pixels[3][3]=3
pixels[4][4]=4
pixels[5][5]=5
pixels[6][6]=6
pixels[7][7]=7
pixels[8][8]=8
pixels[9][9]=9
pixels[9][0]=10
pixels[8][1]=11
pixels[7][2]=12
pixels[6][3]=13
pixels[5][4]=14
pixels[4][5]=15

#print('List of lists:')
#print(pixels)

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim, color):
    #sleep(1)
    myPen.color(colourPalette[color])
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)
    myPen.getscreen().update()
	
boxSize = 10	
#Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)




for i in range (0,len(pixels)):
    for j in range (0,len(pixels[i])):
        #if pixels[i][j]==1:
            #box(boxSize)
        box(boxSize, pixels[i][j])    
        
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()	
    myPen.setheading(270) 
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180) 
    myPen.forward(boxSize*len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()
	
myPen.getscreen().update()	

turtle.Screen().exitonclick() 

#sleep(10)