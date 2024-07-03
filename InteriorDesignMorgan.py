#Morgan Pickens
#11 Oct 23

#Introduction
print("Hello and welcome to Morgan's Interior design program. ")

#input
length = float(input("Insert length: "))
width  = float(input ("Insert width: "))
height = float(input ("Insert height: "))
gallon = float(input("Insert price per gallon of paint: "))
square = float(input("Input price per sqaure foot of flooring: "))

#Round Up
import math
              
#calculation Section
Area = width * height
Volume = length * width * height
Walls = 2*(length * height + width * height)
Ceiling = length * width
Windows = (Walls + Ceiling) - (0.1 *(Walls + Ceiling))
Floor = length * width
Trim = 4 * length + width * 4
PaintTotal = math.ceil(Windows / 350) - Floor 

#Answers to the question 
Question1 = Walls + Ceiling - Windows
Question2 = Floor
Question3 = Area
Question4 = Trim
Question5 = PaintTotal
Question6 = Floor

        
#output section
print("Total area on the walls and ceiling for paint", Question1)
print("Total area on the floor for flooring", Question2)
print("Total room volume for fans and lighting", Question3)
print("Total length along the perimeter for Trim", Question4)
print("Total cost for paint", Question5)
print("Total cost for paint and cost for flooring $", Question6)


#written report
#I went about doing this assignment first by mapping out
#what needed to be done with a flow chart and putting it together.

#I tested this program by running the module mutiple times.
#one case i couldn't get the coreect price of the paint
#second case i coulldn't get the correct price for the fllor
