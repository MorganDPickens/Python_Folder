#Morgan Pickens
#Lab03
#10/14/2023

#we use this to define the main function when we have multiple.
def main():

    #Input section
    base1 =input("Please enter the base1. ")
    base2 =input("Please eneter the base2. ")
    height =input("Pleas eneter the height. ")

    #Convert string into a number
    base1 = float(base1)
    base2 = float(base2)
    height = float(height) 

    #This is the function to define the are of a trapezoid
    def area_of_trapezoid(base1, base2 , height,):
        area = 0.5 * (base1 + base2) * height
        return area

        #Here we must define the keyword "result" in our output
        result = area_of_trapezoid(base1, base2, height)

        #Output section 
        print(f"This is the area of the trapezoid {result}")

#Test 1
#In test 1, I tried to enter this eqution: cone $= \frac{1}{3} \pi \cdot r^2 \cdot h$
#of course, I realized trying to copy and past this equation is not possible.
#In order to use this equation i must convert it to the python equivalent.

#Test 2
#During test 2 i entered the correct equation for Python (1/3) * math.pi * (r ** 2) * h
#but i actually couldn't get it to work. After goin through this problem i realized
#i made the mistake of not importing math

#Test 3 during adding the main() function i was not able to get the code to work because
#of an indent error. I did not understand at first what this means, but i do now
#when using the main function for python recongnize it there must be a indent
#and also for "def area_of_trapezoid" it must be indented inside the indent to include
#it aswell.
        

#Part 2
import math
r =7
h =15

#Here we define the value of the cone.
cone = (1/3) * math.pi * (r ** 2) * h

#Out put volume result 
print("This is the Volume of the cone",cone)

#This statement is required in order to call on the main function
#Test 4: I tried running this program without this statement, and my main function becomes
#unable to be seen. 

if __name__ == "__main__":
    main() 

