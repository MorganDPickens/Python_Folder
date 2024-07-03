
#Morgan Pickens
#10/18/2023
#Savings Calculator

#input section
Savings = float(input("Enter your savings amount, "))
Interest =float(input("Enter your intrest rate 1-100%. "))/100

#This is to convert a percentage to a decmial number



#Calculations (This is assuming a yearly intrest rate
After20=(Savings)+(Savings*Interest*20)
#Calculate Earnings From Intrest
Earned=After20-Savings

#Extra questions (This is not intrested included just to add)
#The problem did not specifiy if i neeeded to ad the intrest
#So this is just the savings. 
Doubled = Savings * 240
ExtraYears = Savings * 360


#test 1
#I couldnt mke my variable a float number so i chose to convert
#the percentage from the input itself

#output section

print("This is your savings amount after 20Years.",After20)
print("This is the intrest earned after 20 years.", Earned)
print("This is the amount if doubled every month for 20 years", Doubled)
print("This is the amount if saved for 30Years.", ExtraYears)

#Question 1
#I approched this assignment by making a flow chat of what i needed

#Question 2
#I Ran test myself with the idle
#I Learned to just divde from the variable input instead of making a seprate one

