# Starter code for homework 6
#Morgan Pickens
#csc110
#11/14/2023


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 800


from Gui import *

#________________________________________________________________________________

                                  #SECTION 1 FIGURES
def figure1(x, y, height, spacing, up=True):
    for i in range(20):
        y_start = y + i * (height + spacing)
        y_end = y_start + height
        direction = 1 if up else -1
        canvas.line([[x, y_start], [x + 120, y_end]], fill='brown')  # adjust width/color

def figure2(x, y, height, spacing, up=True):
    for i in range(5):
        y_start = y + i * (height + spacing)
        y_end = y_start + height
        direction = 1 if up else -1
        canvas.line([[x, y_start], [x + 200, y_start]], fill='purple')  # adjust width/color

def figure3(x, y, height, spacing, up=True):
    for i in range(8):
        y_start = y + i * (height + spacing)
        y_end = y_start + height
        direction = 1 if up else -1
        canvas.line([[x, y_start], [x + 90, y_start]], fill='red')  # adjust width/color

def figure4(x, y, height, spacing, up=True):
    for i in range(10):
        angle = i * (18)  # How Far apart each line is
        x_end = x + (i - 5) * spacing  # Decide where your middle line starts
        y_end = y + height
        direction = 1 if up else -1
        canvas.line([[x, y], [x_end, y_end]], fill='blue', width=1)

def figure5(x, y, height, spacing, up=False):
    for i in range(9):
        angle = i * (18)  # How Far apart each line is
        x_end = x + (i - 4) * spacing  # Decide where your middle line starts
        y_end = y - height
        direction = 1 if up else -1
        canvas.line([[x, y], [x_end, y_end]], fill='Orange', width=1)

def figure6(x, y, height, spacing, up=False):
    for i in range(5):
        angle = i * (150)  # How Far apart each line is
        x_end = x + (i - 2) * spacing  # Decide where your middle line starts
        y_end = y - height
        direction = 1 if up else -1
        canvas.line([[x, y], [x_end, y_end]], fill='Green', width=1)

def main():
    figure1(-200, 260, 0, 5, up=True)
    figure2(135, 0, 50, 1, up=True)
    figure3(-300, -270, 15, -3, up=True)
    figure4(0, 0, 50, 10, up=True)
    figure5(-350, 0, 90, 18, up=False)
    figure6(200, -200, 50, 30, up=False)
#_______________________________________________________________________________

                     #Section 2
#1. How did you go about starting this assignment? where did you get stuck, if
    #at all, and how did you get unstuck?

#I started by reviewing what needed to be completed for the shapes, also what
    #kind of code i would need for the canvas
    #I got suck alot during the positioning of the canvas shapes it took hours
    #to figure out how to fix the shapes to be even

#2. How did you test your program?
    # i tested this program by using the IDLE
    #yes it meets the homeowkr specification.
    #everything works how i wanted it to

#3. I learned for to add another parameter to my functions vs the last assignment
    # that was on gui we used only 3
 



#_______________________________________________________________________________
    

###################################################################
# Feel free to read what's here, but do not change

g = Gui()
g.title('HW6 Lines')

# canvas is the drawing area
canvas = g.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
main()
g.mainloop()

