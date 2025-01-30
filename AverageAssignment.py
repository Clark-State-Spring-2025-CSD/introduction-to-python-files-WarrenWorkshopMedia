#Print a line asking the user to enter three numbers

#Prompt the user to enter the three integers, one at a time

#Display the three numbers entered, their sum, and the average.

#You can assume the user will only enter positive integers

#Example output: (you do not have to match my words exactly)

#Please enter three whole numbers:

#Number 1: 11

#Number 2: 11

#Number 3: 12

#The sum of 11 and 11 and 12 is 34 and the average is 11.333333333333334.

Number1 = 0
Number2 = 0
Number3 = 0

print("please enter three numbers into the terminal.")
Number1 = int(input("Enter First Number: "))

Number2 = int(input("Enter Second Number: "))

Number3 = int(input("Enter Third Number: "))

Sum = Number1 + Number2 + Number3

Average = Sum / 3

print(f"the sum of {Number1}, {Number2}, and {Number3} is {Sum} and the average is {Average}.")