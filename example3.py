

from tkinter import Label, Widget


widgets_dictionary = {} # initialize your empty dictionary

for i in range(rows):
    for j in range(columns):
        # widget definition here, let's say it's a label
        label = Label(...)
        label.pack()
        # create a reference to the widget in your dictionary
        widget[(i,j)] = label

# Now, referring to your specific question:
# (x,y) = the index of the cell you want to change
# colour = the background colour you want to change it to
Widget[(x,y)].config(bg = "colour") 