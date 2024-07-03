# TreeTest3.py
# This sample program demonstrates drawing shapes
# on a canvas using some Gui tools.
#
# Study the sample code that is posted before working with this program.
#
# This program is not interactive.  It draws the same
# picture every time it is executed.
#
# To run this program, you must save the file Gui.py
# in the same folder as this program.
#
# CSC 110
# (Python 3 version)

# Required import statement for Gui tools
import Gui

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section

# Draws one tree.  The parmeters base_x and base_y specify
# the location of a point at the center of the bottom edge
# of the tree trunk.  The last parameter is the height of
# the tree.  All parameters have units of pixels.
def draw_simple_tree(base_x, base_y, height):
    # draw trunk
    trunk_x1 = base_x - height * 0.05  # trunk width is 10% of tree height
    trunk_x2 = base_x + height * 0.05
    trunk_y1 = base_y
    trunk_y2 = base_y + height * 0.5 # trunk height is 50% of tree height
    canvas.rectangle([[trunk_x1, trunk_y1], [trunk_x2, trunk_y2]], \
                     fill='yellow', width = 0)
    # draw crown
    # the polygon has 3 points, peak, lower left (LL), and lower right (LR)
    LL_x = base_x - height * 0.2 # crown width is 40% of tree height
    LR_x = base_x + height * 0.2
    L_y = base_y + height * 0.3  # crown starts 30% up from the bottom
    canvas.polygon([[base_x, base_y + height], [LL_x, L_y], [LR_x, L_y]], \
                   fill='lightgreen', width=0)

    # draw a test line, using the parameters, to ensure the drawing
    # is accurate
    # tree is supposed to be rooted at (base_x, base_y) with the given height
    canvas.line([[base_x, base_y], [base_x, base_y + height]])

# Draws a cluster of three trees.  The parmeters x and y specify
# the location of a point at the center of the bottom edge
# of the tree trunk of the largest tree in the cluster.
# The last parameter is the "size" of the cluster -- the distance
# in pixels from the bottom to the top of the cluster.
def draw_tree_cluster(x, y, size):
    draw_simple_tree(x - size * 0.15, y + size * 0.5, size * 0.5)
    draw_simple_tree(x - size * 0.3, y + size * 0.3, size * 0.6)
    draw_simple_tree(x, y, size * 0.8)

    # this last tree is the largest, so we use a vertical line to confirm
    # we use the parameters correctly - according to the function block comments
    # (x,y) is the center of the largest tree. size is the height of the cluster
    canvas.line([[x,y], [x, y + size]])


#------------------------------------------------------------------------------------------
#Morgan Pickens
#24 Oct 23
#HM04

#Function 1 shape 1 
#------------------------------------------------------------------------------------------

#This is the function to draw the sun
def draw_yellow_sun(x, y, radius, color):
    # Draw the sun (a circle)
    canvas.oval([[x - radius, y - radius], [x + radius, y + radius]], fill='yellow', width=0)


    #canvas.line([[x,y - radius], [x, y + radius]])
 

#Function 1 Shape 2
#-----------------------------------------------------------------------------------------

 # Right-pointing triangle
    triangle_x1 = x + radius
    triangle_y1 = y - radius
    triangle_x2 = x + radius + 50# Adjust the size and position of the triangle
    triangle_y2 = y
    triangle_x3 = x + radius
    triangle_y3 = y + radius
    canvas.polygon([[triangle_x1, triangle_y1], [triangle_x2, triangle_y2], [triangle_x3, triangle_y3]], fill=color, width=0)
      
    


#Function 1 Shape 3 
#----------------------------------------------------------------------------------------


  # Upward-pointing triangle
    triangle_x4 = x - radius
    triangle_y4 = y + radius
    triangle_x5 = x
    triangle_y5 = y + radius + 50  # Adjust the size and position of the triangle
    triangle_x6 = x + radius
    triangle_y6 = y + radius
    canvas.polygon([[triangle_x4, triangle_y4], [triangle_x5, triangle_y5], [triangle_x6, triangle_y6]], fill=color, width=0)

#Function 1 shape 4
#------------------------------------------------------------------------------------------

# Triangle
    triangle_x4 = x - radius
    triangle_y4 = y - radius
    triangle_x5 = x - radius - 50  # Adjust the size and position of the triangle
    triangle_y5 = y
    triangle_x6 = x - radius
    triangle_y6 = y + radius
    canvas.polygon([[triangle_x4, triangle_y4], [triangle_x5, triangle_y5], [triangle_x6, triangle_y6]], fill=color, width=0)
    
#-----------------------------------------------------------------------------------------
#Function 2 Shape 1 House

#Draw the foundation of the house
def draw_square(x, y, side_length, color):
    canvas.rectangle([[x - side_length / 2, y - side_length / 2], [x + side_length / 2, y + side_length / 2]], fill=color, width=0)

#-----------------------------------------------------------------------------------------
    #Function 2 shape 2
    
    # Draw one downward-pointing triangle
    triangle_x1 = x - side_length / 2
    triangle_y1 = y + side_length / 2
    triangle_x2 = x + side_length / 2
    triangle_y2 = y + side_length / 2
    triangle_x3 = x
    triangle_y3 = y + side_length
    canvas.polygon([[triangle_x1, triangle_y1], [triangle_x2, triangle_y2], [triangle_x3, triangle_y3]], fill='red', width=0)

    #Function 2 shape 3
    
 #  window
    window_size = side_length * 0.4  # Adjust the size of the window
    window_x1 = x - window_size / 2
    window_y1 = y - window_size / 2
    window_x2 = x + window_size / 2
    window_y2 = y + window_size / 2
    canvas.rectangle([[window_x1, window_y1], [window_x2, window_y2]], fill='black', width=0)

     #Function 2 shape 4

     #window
    circle_radius = window_size / 2
    circle_x = x
    circle_y = (triangle_y1 + window_y2) / 3.1
    canvas.oval([[circle_x - circle_radius, circle_y - circle_radius], [circle_x + circle_radius, circle_y + circle_radius]], fill='black', width=0)
    #canvas.line([[x,y - side_length], [x, y + side_length]])

#---------------------------------------------------------------------------------------------
    #Function 3 

def draw_cloud(x, y, cloud_radius):
    cloud_color = 'cyan'  # You can change the color
    canvas.oval([[x - cloud_radius, y - cloud_radius], [x + cloud_radius, y + cloud_radius]], fill=cloud_color)

    #Secound cloud
    canvas.oval([[x + cloud_radius * 2.0, y - cloud_radius * 0.8], [x + cloud_radius * -0.11, y + cloud_radius * 0.6]], fill=cloud_color)
    #Third cloud
    canvas.oval([[x - cloud_radius * 1.7, y - cloud_radius * 0.9], [x + cloud_radius * 0.3, y + cloud_radius * 0.6]], fill=cloud_color)
    #canvas.line([[x,y - cloud_radius], [x, y + cloud_radius]])


#----------------------------------------------------------------------------------------------
    #Function 4
    #Lightning bolts
def draw_light(x, y, light_radius):    
    lightning_length = light_radius * 0.8  # Adjust the size of the lightning bolts
    lightning_x1 = x + lightning_length * 2.0
    lightning_y1 = y - lightning_length * 2.0
    #Second bolts
    lightning_x2 = x - lightning_length * 2.0
    lightning_y2 = y - lightning_length * 2.0
    canvas.line([[lightning_x1, lightning_y1], [x, y]], fill='yellow', width=8)
    canvas.line([[x, y], [lightning_x2, lightning_y2]], fill='yellow', width=8)
    #canvas.line([[x,y - light_radius], [x, y + light_radius]])
    
#-------------------------------------------------------------------------------------------







def main():
    # Master Tool For Canvas drawing Functions
    draw_tree_cluster(0, 0, 50)
    draw_tree_cluster(-40, -30, 65)
    draw_tree_cluster(60, -120 , 120)
    draw_simple_tree(80, 10, 100)
    draw_simple_tree(-100, -180, 160)
    draw_yellow_sun(200, 120, 50, 'yellow')
    draw_square(200,-100,75,'blue')
    draw_cloud(-150,175,50)
    draw_light(-150,140,50)





#How did i go tabout starting this assignement?
    #I started this assignment by visiulizing what i wanted to make and how i was going to implement that into my code.

#How did i test my program?
    #testing it was kinda annoying i had to keep saving and running over and over to see my work
#what did i learn from this assignment?
    #I learned edit the size of my shapes on the canvas and the positioning by using x and y parameters




#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: http://tmml.sourceforge.net/doc/tk/colors.html
